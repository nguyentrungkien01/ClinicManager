var gIndexHintIdCard = null
var gIndexHintMedicineName = null
var isCreated = true
var gOrderId = null

function getCurrentDoctorInfo() {
    fetch('/api/current_doctor', {
        method: 'post',
        body: {},
        headers: {
            'Content-Type': 'application/json'

        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        $('#current_doctor_info').text(datas['info'])
    })
}


function getCustomerIdCard() {
    fetch('/api/customer_id_card_doctor', {
        method: 'post',
        body: JSON.stringify({
            'id_card': $('#id_card_input').val() == undefined ? null : $('#id_card_input').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        if (datas.length > 0)
            gIndexHintIdCard = 1
        var row = ''
        for (let i = 0; i < datas.length; i++)
            row += `<p onclick = "onClickHintCustomerIdCard('${datas[i]['value']}')"
            onmouseover="onMouseOverHintCustomerIdCard(${i + 1})">
                ${datas[i]['value']}</p>`
        $('#result_id_card').html(row)
    })
}

function getMedicineName() {
    fetch('/api/medicine_name_doctor', {
        method: 'post',
        body: JSON.stringify({
            'medicine_name': $('#medicine_name_input').val() == undefined ? null : $('#medicine_name_input').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        if (datas.length > 0)
            gIndexHintMedicineName = 1
        var row = ''
        for (let i = 0; i < datas.length; i++)
            row += `<p onclick = "onClickHintMedicineName('${datas[i]['value']}')"
            onmouseover="onMouseOverHintMedicineName(${i + 1})">
                ${datas[i]['value']}</p>`
        $('#result_name_medicine').html(row)
    })
}

function getMedicineUnit(OrderId) {
    fetch('/api/medicine_unit_doctor', {
        method: 'post',
        body: JSON.stringify({
            'medicine_name': $('#medicine_name_input').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        console.info(datas)
        $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(5)`).text(datas[0]['value'])

    })
}

function checkMedicineName() {
    fetch('/api/check_medicine_name_doctor', {
        method: 'post',
        body: JSON.stringify({
            'medicine_name': $('#medicine_name_input').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        var medicineName = $('#medicine_name_input').val()
        var dosage = $('#dosage').val()
        var usingMethod = $('#using_method').val()
        if (medicineName == null || medicineName.length <= 0) {
            Swal.fire({
                title: 'Tên thuốc không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })

            // .then((result) => {
                
            //     if (result.isConfirmed) {
            //       Swal.fire('Saved!', '', 'success')
            //     } else if (result.isDenied) {
            //       Swal.fire('Changes are not saved', '', 'info')
            //     }
            //   })
            return
        }
        if (dosage == null || dosage.length <= 0) {
            Swal.fire({
                title: 'Thông tin liều dùng không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (usingMethod == null || usingMethod.length <= 0) {
            Swal.fire({
                title: 'Phương pháp sử dụng không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (!(datas.length > 0)) {
            Swal.fire({
                title: 'Thuốc không tồn tại',
                icon: 'error',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (isCreated) {
            addMedicine()
            getMedicineUnit($('#medicine_datas').children().length)
        } else {
            saveEditMedicine(gOrderId)
            gOrderId = null
        }

    })
}

function checkCustomerIdCard() {
    fetch('/api/check_customer_id_card_doctor', {
        method: 'post',
        body: JSON.stringify({
            'id_card': $('#id_card_input').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        var idCard = $('#id_card_input').val()
        var symptom = $('#symptom').val()
        var predictedDisease = $('#predicted_disease').val()
        if (idCard == null || idCard.length <= 0) {
            Swal.fire({
                title: 'Thông tin CCCD không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (symptom == null || symptom.length <= 0) {
            Swal.fire({
                title: 'Thông tin triệu chứng không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (predictedDisease == null || predictedDisease.length <= 0) {
            Swal.fire({
                title: 'Thông tin bệnh chuẩn đoán không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if (!(datas.length > 0)) {
            Swal.fire({
                title: 'Khách hàng không tồn tại',
                icon: 'error',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        if ($('#medicine_datas').children().length <= 0) {
            Swal.fire({
                title: 'Danh sách thuốc không được để trống',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        //save and export
        saveData()
    })
}

function saveData() {
    var medicine_list = []
    for (let i = 1; i <= $('#medicine_datas').children().length; i++)
        medicine_list.push({
            'name': $(`#medicine_datas tr:nth-child(${i}) td:nth-child(3)`).text().trim(),
            'amount': $(`#medicine_datas tr:nth-child(${i}) td:nth-child(4) span`).text().trim(),
            'dosage': $(`#medicine_datas tr:nth-child(${i}) td:nth-child(6)`).text().trim(),
            'using_method': $(`#medicine_datas tr:nth-child(${i}) td:nth-child(7)`).text().trim(),
        })

    fetch('/api/save_medical_examination_data', {
        method: 'post',
        body: JSON.stringify({
            'id_card': $('#id_card_input').val(),
            'symptom': $('#symptom').val(),
            'predicted_disease': $('#predicted_disease').val(),
            'medicine_list': medicine_list
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        if (datas['result']) {
            exportPDF()
            Swal.fire({
                title: 'Tạo phiếu khám mới thành công',
                icon: 'success',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            clearData()
        } else {
            Swal.fire({
                title: 'Tạo phiếu khám thất bại',
                text: 'Vui lòng thử lại',
                icon: 'error',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
        }
    })
}


// id card action
function onClickHintCustomerIdCard(hint) {
    $('#id_card_input').val(hint.trim())
    $('#result_id_card').html('')
}

function onMouseOverHintCustomerIdCard(position) {
    gIndexHintIdCard = position
    for (let i = 1; i <= $('#result_id_card').children().length; i++)
        $(`.id-card-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
    $(`.id-card-choice .show-hint p:nth-child(${position})`).css("background-color", "#04a9f5");

}

// medicine name action
function onClickHintMedicineName(hint) {
    $('#medicine_name_input').val(hint.trim())
    $('#result_name_medicine').html('')
}

function onMouseOverHintMedicineName(position) {
    gIndexHintMedicineName = position
    for (let i = 1; i <= $('#result_name_medicine').children().length; i++)
        $(`.medicine-name-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
    $(`.medicine-name-choice .show-hint p:nth-child(${position})`).css("background-color", "#04a9f5");

}
//controller medicine table
function addMedicine() {
    var order_id = $('#medicine_datas').children().length + 1
    var nameMedicine = $('#medicine_name_input').val()
    for (let i = 1; i <= $('#medicine_datas').children().length; i++)
        if (nameMedicine == $(`#medicine_datas tr:nth-child(${i}) td:nth-child(3)`).text().trim()) {
            Swal.fire({
                title: 'Tên thuốc đã tồn tại',
                icon: 'error',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }

    var amountMedicine = $('#medicine_amount').val()
    var dosage = $('#dosage').val()
    var usinMethod = $('#using_method').val()

    var row = `<tr>
        <td> 
        <i class="far fa-trash-alt" onclick = "removeMedicine(${order_id})"></i>
        <i class="far fa-edit" onclick = "editMedicine(${order_id})"></i>
        </td>
        <td>${order_id}</td>
        <td>${nameMedicine} </td>
        <td><span>${amountMedicine}</span>
            <a href="javascript:;" class="btn btn-xs btn-secondary btn-success "onclick = "addAmount(${order_id})"> + </a>
            <a href="javascript:;" class="btn btn-xs btn-secondary btn-danger "onclick = "subtractAmount(${order_id})"> - </a>
        </td>
        <td></td>
        <td>${dosage}</td>
        <td>${usinMethod}</td>
        </tr>`
    $('#medicine_datas').append(row)
    $('#add_medicine_modal').modal('toggle')
}

function editMedicine(OrderId) {
    isCreated = false
    $('#add_medicine_modal').modal('toggle')
    var element = $(`#medicine_datas tr:nth-child(${OrderId})`)
    var name = $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(3)`).text()
    var amount = parseInt($(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(4) span`).text())
    var dosage = $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(6)`).text()
    var usingMethod = $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(7)`).text()
    $('#medicine_name_input').val(name)
    $('#medicine_amount').val(amount)
    $('#dosage').val(dosage)
    $('#using_method').val(usingMethod)
    gOrderId = OrderId
}

function saveEditMedicine(OrderId) {
    for (let i = 1; i <= $('#medicine_datas').children().length; i++)
        if ($('#medicine_name_input').val() == $(`#medicine_datas tr:nth-child(${i}) td:nth-child(3)`).text().trim() && OrderId != i) {
            alert('Ten thuoc da ton tai')
            return
        }
    $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(3)`).text($('#medicine_name_input').val())
    $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(4) span`).text($('#medicine_amount').val())
    $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(6)`).text($('#dosage').val())
    $(`#medicine_datas tr:nth-child(${OrderId}) td:nth-child(7)`).text($('#using_method').val())
    getMedicineUnit(OrderId)
    isCreated = true
}

function removeMedicine(order_id) {
    $(`#medicine_datas tr:nth-child(${order_id})`).remove()
    for (let i = 1; i <= $('#medicine_datas').children().length; i++)
        $(`#medicine_datas tr:nth-child(${i}) td:nth-child(2)`).text(i)
}

function addAmount(order_id) {
    var element = $(`#medicine_datas tr:nth-child(${order_id}) td:nth-child(4) span`)
    var amount = parseInt(element.text())
    amount++
    element.text(amount)
}

function subtractAmount(order_id) {
    var element = $(`#medicine_datas tr:nth-child(${order_id}) td:nth-child(4) span`)
    var amount = parseInt(element.text())
    amount--
    if (amount < 1)
        amount = 1
    element.text(amount)
}

// export pdf
function exportPDF() {
    var today = new Date();
    var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + ' ' + time;
    const pdf = new jsPDF({
        orientation: 'portrait',
        format: 'a4',
        putOnlyUsedFonts: true,
        floatPrecision: 16
    })
    pdf.setFontSize(13)
    pdf.text('MEDICAL EXAMINATION', 77, 10)
    pdf.text(`Customer's identity card: ${$('#id_card_input').val()}`, 10, 20)
    pdf.text(`Time: ${dateTime}`, 10, 40)
    pdf.text(`Symptom: ${$('#dosage').val()}`, 10, 60)
    pdf.text(`Predicted desease: ${$('#predicted_disease').val()}`, 10, 80)
    pdf.text(`Doctor: ${$('#current_doctor_info').text()}`, 10, 100)
    pdf.text('MEDICINE LIST', 85, 120)
    var head = ['Ordered id', 'Name', 'Amount', 'Unit', 'Dosage', 'Using method']
    var body = []
    for (let i = 1; i <= $('#medicine_datas').children().length; i++) {
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(2)`).text())
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(3)`).text())
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(4) span`).text())
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(5)`).text())
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(6)`).text())
        body.push($(`#medicine_datas tr:nth-child(${i}) td:nth-child(7)`).text())
    }
    pdf.autoTable({
        head: [head],
        body: [body],
        startY: 140,
        theme: 'grid',
        styles: {
            font: 'Arial',
            fontStyle: 'normal',
        },
        lang: 'vi',
        headStyles: {
            fontStyle: 'bold',
            halign: 'center',
            valign: 'middle',
            fontSize: 13,
            cellWidth: 'auto',
            minCellHeight: 15,
            lineWidth: 1,
            lineColor: [4, 41, 58]
        },
        bodyStyles: {
            halign: 'center',
            valign: 'center',
            lineColor: [4, 41, 58],
            cellPadding: {
                bottom: 5,
                top: 5
            }
        }
    })
    pdf.autoPrint({
        variant: 'non-conform'
    });
    pdf.save('medical examination.pdf')
}

//clear data
function clearData() {
    $('#id_card_input').val('')
    $('#symptom').val('')
    $('#predicted_disease').val('')
    $('#medicine_datas').html('')
}

$(document).ready(function () {
    //info current doctor
    getCurrentDoctorInfo()

    // id card input
    $('#result_id_card').hide()

    $('#id_card_input').on('input', function () {
        $('#result_id_card').show()
        getCustomerIdCard()
    })
    $('#id_card_input').focus(function () {
        $('#result_id_card').show()
        if (gIndexHintIdCard != null)
            $(`.id-card-choice .show-hint p:nth-child(1)`).css("background-color", "#04a9f5");

    })
    $('#id_card_input').keydown(function (event) {
        if (gIndexHintIdCard == null)
            return;
        if (event.keyCode == 13) {
            event.preventDefault()
            $('#id_card_input').val($(`.id-card-choice .show-hint p:nth-child(${gIndexHintIdCard})`).text().trim())
            $('#result_id_card').html('')
        }

        if (event.keyCode == 40) {
            for (let i = 1; i <= $('#result_id_card').children().length; i++)
                $(`.id-card-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (++gIndexHintIdCard > $('#result_id_card').children().length)
                gIndexHintIdCard = 1
            $(`.id-card-choice .show-hint p:nth-child(${gIndexHintIdCard})`).css("background-color", "#04a9f5");

        }
        if (event.keyCode == 38) {
            for (let i = 1; i <= $('#result_id_card').children().length; i++)
                $(`.id-card-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (--gIndexHintIdCard <= 0)
                gIndexHintIdCard = $('#result_id_card').children().length
            $(`.id-card-choice .show-hint p:nth-child(${gIndexHintIdCard})`).css("background-color", "#04a9f5");

        }
    })

    // medicine name input 
    $('#result_name_medicine').hide()

    $('#medicine_name_input').on('input', function () {
        $('#result_name_medicine').show()
        getMedicineName()
    })
    $('#medicine_name_input').focus(function () {
        $('#result_name_medicine').show()
        if (gIndexHintMedicineName != null)
            $(`.medicine-name-choice .show-hint p:nth-child(1)`).css("background-color", "#04a9f5");

    })
    $('#medicine_name_input').keydown(function (event) {
        if (gIndexHintMedicineName == null)
            return;
        if (event.keyCode == 13) {
            event.preventDefault()
            $('#medicine_name_input').val($(`.medicine-name-choice .show-hint p:nth-child(${gIndexHintMedicineName})`).text().trim())
            $('#result_name_medicine').html('')
        }

        if (event.keyCode == 40) {
            for (let i = 1; i <= $('#result_name_medicine').children().length; i++)
                $(`.medicine-name-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (++gIndexHintMedicineName > $('#result_name_medicine').children().length)
                gIndexHintMedicineName = 1
            $(`.medicine-name-choice .show-hint p:nth-child(${gIndexHintMedicineName})`).css("background-color", "#04a9f5");

        }
        if (event.keyCode == 38) {
            for (let i = 1; i <= $('#result_name_medicine').children().length; i++)
                $(`.medicine-name-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (--gIndexHintMedicineName <= 0)
                gIndexHintMedicineName = $('#result_name_medicine').children().length
            $(`.medicine-name-choice .show-hint p:nth-child(${gIndexHintMedicineName})`).css("background-color", "#04a9f5");

        }
    })

    //controller medicine tables
    $('#add_medicine').click(function () {
        $('#medicine_name_input').val('')
        $('#medicine_amount').val(1)
        $('#dosage').val('')
        $('#using_method').val('')
        isCreated = true
    })


    // confirm button
    $('#cfm_button').click(function () {
        checkMedicineName()
    })


    // save and export pdf
    $('#save_export_button').click(function () {
        checkCustomerIdCard()
    })
})