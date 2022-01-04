window.onload = function () {
    $("#search_result").modal("toggle");
  };
  
function confirm_pay() {
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
            alert("Thanh toan thanh cong!");
            exportPDF();
            resetData();
            return;
        }
        alert("Thanh toan that bai! Vui long kiem tra lai");
    });
}
function resetData() {
    $("#bill_detail").hide();
}

function exportPDF() {
    const pdf = new jsPDF({
        orientation: "portrait",
        format: "a4",
        putOnlyUsedFonts: true,
        floatPrecision: 16,
    });
    pdf.setFontSize(13);
    pdf.text("MEDICAL BILL", 77, 10);
    pdf.text(`Customer's fullname: ${$("#customer_fullname_pay").text()}`, 10,20)
    pdf.text(`Customer's date of birth: ${$("#date_of_birth_pay").text()}`, 10, 30)
    pdf.text(`Customer's sex: ${$("#sex_pay").text()}`, 10, 40)
    pdf.text(`Customer's id card: ${$("#customer_id_pay").text()}`, 10, 50)
    pdf.text(`Medical examination id: ${$("#medical_examination_id_pay").text()}`, 10, 60)
    pdf.text(`Doctor's fullname: ${$("#doctor_fullname_pay").text()}`, 10, 70)
    pdf.text(`Doctor's code: ${$("#doctor_code_pay").text()}`, 10, 80)
    pdf.text(`Nurse's fullname: ${$("#nurse_fullname_pay").text()}`, 10, 90)
    pdf.text(`Nurse's code: ${$("#nurse_code_pay").text()}`, 10, 100)
    pdf.text("MEDICINE LIST", 85, 120)
    var head = [
        "Id",
        "Name",
        "Unit",
        "Amount",
        "Unit price",
        "Total price",
    ]
    var body = [];
    for (let i = 1; i <= $("#medicine_list_datas").children().length; i++){
        row=[]
        for (let j = 1; j <= head.length; j++)
            row.push($(`#medicine_list_datas tr:nth-child(${i}) td:nth-child(${j})`).text())
        body.push(row)
    }

    pdf.autoTable({
        head: [head],
        body: body,
        startY: 130,
        theme: "grid",
        styles: {
            font: "Arial",
            fontStyle: "normal",
        },
        lang: "vi",
        headStyles: {
            fontStyle: "bold",
            halign: "center",
            valign: "middle",
            fontSize: 13,
            cellWidth: "auto",
            minCellHeight: 15,
            lineWidth: 1,
            lineColor: [4, 41, 58],
        },
        bodyStyles: {
            halign: "center",
            valign: "center",
            lineColor: [4, 41, 58],
            cellPadding: {
                bottom: 5,
                top: 5,
            },
        },
    });

    pdf.text(`Total medicine price: ${$("#medicine_price_total_pay").text()}`, 10, pdf.lastAutoTable.finalY + 10);
    pdf.text(`Total medicinal examination price: ${$("#medical_examination_price_pay").text()}`, 10, pdf.lastAutoTable.finalY + 20);
    pdf.text(`Total payment: ${$("#total_price_pay").text()}`, 10, pdf.lastAutoTable.finalY + 30);

    pdf.autoPrint({
        variant: "non-conform",
    });
    pdf.save("medical examination.pdf");
}

$(document).ready(function () {
    $("#confirm").click(function () {
        confirm_pay();
    });
});
