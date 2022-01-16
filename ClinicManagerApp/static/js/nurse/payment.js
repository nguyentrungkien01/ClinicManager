window.onload = function () {
    $("#search_result").modal("toggle");
};

function confirmPay() {
    fetch("/api/nurse/payment", {
        method: "post",
        body: JSON.stringify({
            medical_examination_id: $("#medical_examination_id_pay").text(),
        }),
        headers: {
            "Content-Type": "application/json",
        },
    }).then(function (res) {
        return res.json();
    }).then(function (datas) {
        if (datas["result"]) {
            Swal.fire({
                title: 'Thanh toán thành công',
                text: 'Đã xuất phiếu khám',
                icon: 'success',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            exportPDF();
            resetData();
            return;
        }
        Swal.fire({
            title: 'Thanh toán thất bại',
            text: 'Vui lòng kiểm tra lại',
            icon: 'error',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Ok',
        })
    });
}

function resetData() {
    $("#bill_detail").hide();
}

function exportPDF() {
    var today = new Date();
    var date = today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + ' ' + time;
    const pdf = new jsPDF({
        orientation: "portrait",
        format: "a4",
        putOnlyUsedFonts: true,
        floatPrecision: 16,
    });
    pdf.setFontSize(13);
    pdf.text("HOA DON THANH TOAN", 77, 10);
    pdf.text(`Ho Ten: ${$("#customer_fullname_pay").text()}`, 10, 20)
    pdf.text(`Ngay kham: ${dateTime}`, 110, 20)
    pdf.text(`Tien kham: ${$("#medical_examination_price_pay").text()}`, 10, 30);
    pdf.text(`Tien thuoc: ${$("#medicine_price_total_pay").text()}`, 110, 30);
    pdf.text(`Tong tien: ${$("#total_price_pay").text()}`, 10, 40);

    pdf.autoPrint({
        variant: "non-conform",
    });
    pdf.save("medical examination.pdf");
}

$(document).ready(function () {
    $("#confirm").click(function () {
        confirmPay();
    });
});