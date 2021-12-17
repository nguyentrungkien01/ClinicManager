var gMonth = null
var gQuarter = null
var gYear = null
var gPageSize = null
var gBegIdx = null
var gEndIdx = null
var gExportDatas = null
var gCurrentPage = null

function getData() {
    fetch('/api/report', {
        method: 'post',
        body: JSON.stringify({
            'report_type': $('#report_type').val() == undefined ? 'revenue' : $('#report_type').val(),
            'month': gMonth,
            'quarter': gQuarter,
            'year': gYear,
            'begin_index': gBegIdx,
            'end_index': gEndIdx
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setDataTable(datas)
    }).then(function (err) {
        console.info(err)
    })
}

function getAmount() {
    fetch('/api/amount_report', {
        method: 'post',
        body: JSON.stringify({
            'report_type': $('#report_type').val() == undefined ? 'revenue' : $('#report_type').val(),
            'month': gMonth,
            'quarter': gQuarter,
            'year': gYear
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setPagegination(datas)
        if (parseInt(datas['amount']) == 0)
            $('#export_pdf').hide()
        else
            $('#export_pdf').show()

    }).then(function (err) {
        console.info(err)
    })
}
function getAll() {
    fetch('/api/export_report', {
        method: 'post',
        body: JSON.stringify({
            'report_type': $('#report_type').val() == undefined ? 'revenue' : $('#report_type').val(),
            'month': gMonth,
            'quarter': gQuarter,
            'year': gYear
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        gExportDatas = datas
    }).then(function (err) {
        console.info(err)
    })
}



function setPagegination(datas) {
    var page = ''
    var amountData = parseInt(datas['amount'])
    var amountPage = Math.ceil(amountData / gPageSize)
    if (amountPage == 0)
        return
    if (amountPage != 1) {
        gCurrentPage = 1
        $('#pagination').html('')
        page += `<li class="page-item" id ='previous_item'>
                <button class="page-link" onclick='setPrevious(${amountPage} )'>Truoc</button>
            </li>`
        for (let i = 1; i <= amountPage; i++)
            page += `<li class="page-item ${i == 1 ? 'active' : ''}">
                    <button class="page-link" onclick='setPage(${i},${amountPage})'>${i}</button>
                </li>`

        page += `<li class="page-item" id = 'next_item'>
                <button class="page-link" onclick='setNext(${amountPage}, ${amountData})'>Sau</button>
            </li>`
        $('#pagination').html(page)
    }
}

function setPrevious(amountPage) {
    if (gBegIdx - gPageSize >= 0) {
        $('#previous_item').show()
        gCurrentPage--;
        if (gCurrentPage == 1)
            $('#previous_item').hide()

        if (gCurrentPage == 1 && gCurrentPage != amountPage)
            $('#next_item').show()


        gBegIdx -= gPageSize
        gEndIdx = gBegIdx + gPageSize
        getData()
    }
    else {
        $('#previous_item').hide()
    }
    $('#pagination').children().removeClass('active')
    $(`#pagination li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setNext(amountPage, amountData) {

    if (gBegIdx + gPageSize <= amountData) {
        $('#next_item').show()
        gCurrentPage++;
        if (gCurrentPage == amountPage)
            $('#next_item').hide()
        if (gCurrentPage == amountPage && gCurrentPage != 1)
            $('#previous_item').show()

        gBegIdx += gPageSize
        gEndIdx = gBegIdx + gPageSize
        getData()
    } else {
        $('#next_item').hide()
    }
    $('#pagination').children().removeClass('active')
    $(`#pagination li:nth-child(${gCurrentPage + 1})`).addClass('active')
}
function setPage(itemIdx, amountPage) {
    gCurrentPage = itemIdx
    if (itemIdx == amountPage) {
        $('#next_item').hide()
        if (itemIdx != 1)
            $('#previous_item').show()
    }
    else
        if (itemIdx == 1) {
            $('#previous_item').hide()
            if (itemIdx != amountPage)
                $('#next_item').show()

        }
        else {
            $('#previous_item').show()
            $('#next_item').show()
        }
    gBegIdx = (itemIdx - 1) * gPageSize
    gEndIdx = gBegIdx + gPageSize
    getData()
    $('#pagination').children().removeClass('active')
    $(`#pagination li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setDataSelection() {
    var minYear = 2021
    var maxYear = 2100
    var options = ''
    for (let i = 1; i <= 12; i++)
        options += `<option value=${i}>${i}</option>`
    $('#month_input').html(options)
    options = ''
    for (let i = 1; i <= 4; i++)
        options += `<option value=${i}>${i}</option>`
    $('#quarter_input').html(options)
    options = ''
    for (let i = minYear; i <= maxYear; i++)
        options += `<option value=${i}>${i}</option>`
    $('#year_input').html(options)
}

function setDataTable(datas) {
    if (datas == undefined)
        return
    var headers = ''
    var rows = ''
    $('#title_report_table').html('')
    $('#data_report_table').html('')
    if ($('#report_type').val() == 'revenue') {
        headers += `<tr>
                        <th> ${'Số thứ tự'}</th>
                        <th> ${'Ngày tạo'}</th>
                        <th> ${'Số lượng'}</th>
                        <th> ${'Doanh thu'}</th>
                        <th> ${'Tỷ lệ'}</th>
                    </tr>`

        for (let i = 0; i < datas.length; i++) {
            rows += `<tr>
                        <td>${i + 1}</td>
                        <td>${datas[i]['date']}</td>
                        <td>${datas[i]['amount']}</td>
                        <td>${datas[i]['revenue']}</td>
                        <td>${datas[i]['rate']}</td>
                </tr>`
        }
    }
    if ($('#report_type').val() == 'frequency_of_medicine_use') {
        headers += `<tr>
                        <th> ${'Số thứ tự'}</th>
                        <th> ${'Tên thuốc'}</th>
                        <th> ${'Đơn vị thuốc'}</th>
                        <th> ${'Số lượng thuốc'}</th>
                        <th> ${'Số lần dùng'}</th>
                    </tr>`
        for (let i = 0; i < datas.length; i++)
            rows += `<tr>
                        <td>${i + 1}</td>
                        <td>${datas[i]['medicine_name']}</td>
                        <td>${datas[i]['medicine_unit']}</td>
                        <td>${datas[i]['medicine_amount']}</td>
                        <td>${datas[i]['examination_amount']}</td>
                </tr>`

    }
    if (datas.length > 0) {
        $('#title_report_table').html(headers)
        $('#data_report_table').html(rows)
    }
}



$(document).ready(function () {
    setDataSelection()
    gMonth = parseInt($('#month_input').val())
    gYear = parseInt($('#year_input').val())
    gPageSize = 10
    gBegIdx = 0
    gEndIdx = gBegIdx + gPageSize
    getData()
    getAmount()



    $('#quarter_selection').hide()
    $('#report_type').change(function () {
        gBegIdx = 0
        gEndIdx = gBegIdx + gPageSize
        getData()
        getAmount()
    })

    $('#report_condition').change(function () {
        if ($(this).val() == 'month_report') {
            $('#month_selection').show()
            $('#quarter_selection').hide()
            gMonth = parseInt($('#month_input').val())
            gQuarter = null
        }
        if ($(this).val() == 'quarter_report') {
            $('#month_selection').hide()
            $('#quarter_selection').show()
            gMonth = null
            gQuarter = parseInt($('#quarter_input').val())
        }
        if ($(this).val() == 'year_report') {
            $('#month_selection').hide()
            $('#quarter_selection').hide()
            gMonth = null
            gQuarter = null
        }
        gYear = parseInt($('#year_input').val())
        gBegIdx = 0
        gEndIdx = gBegIdx + gPageSize
        getData()
        getAmount()

    })

    $('#month_input').change(function () {
        gMonth = parseInt($(this).val())
        gBegIdx = 0
        gEndIdx = gBegIdx + gPageSize
        getData()
        getAmount()

    })

    $('#quarter_input').change(function () {
        gQuarter = parseInt($(this).val())
        gBegIdx = 0
        gEndIdx = gBegIdx + gPageSize
        getData()
        getAmount()

    })

    $('#year_input').change(function () {
        gYear = parseInt($(this).val())
        gBegIdx = 0
        gEndIdx = gBegIdx + gPageSize
        getData()
        getAmount()

    })
    $('#export_pdf').mousedown(function () {
        getAll()
    })
    $('#export_pdf').click(function () {
        const pdf = new jsPDF({
            orientation: 'landscape',
            format: 'a4',
            putOnlyUsedFonts: true,
            floatPrecision: 16
        })
        pdf.setFontSize(13)
        var head = []
        var body = []
        var foot = ''
        if ($('#report_type option:selected').val() == 'revenue') {
            head = ['So thu tu', 'Ngay tao', 'So luong', 'Doanh thu', 'Ti le']
            var sum = 0
            for (let i = 0; i < gExportDatas.length; i++) {
                body.push(i + 1)
                body.push(gExportDatas[i]['date'])
                body.push(gExportDatas[i]['amount'])
                body.push(gExportDatas[i]['revenue'])
                sum += parseFloat(gExportDatas[i]['revenue'].slice(0, gExportDatas[i]['revenue'].length - 4).replaceAll(',', ''))
                body.push(gExportDatas[i]['rate'])
            }
            foot = `Tong doanh thu: ${sum} VND`
        }
        if ($('#report_type option:selected').val() == 'frequency_of_medicine_use') {
            head = ['So thu tu', 'Ten thuoc', 'Don vi thuoc', 'So luong', 'So lan dung']
            for (let i = 0; i < gExportDatas.length; i++) {
                body.push(i + 1)
                body.push(gExportDatas[i]['medicine_name'])
                body.push(gExportDatas[i]['medicine_unit'])
                body.push(gExportDatas[i]['medicine_amount'])
                body.push(gExportDatas[i]['examination_amount'])
            }
        }
        pdf.text($('#report_type option:selected').text(), 10, 10, { align: 'center', lang: 'vi' })
        pdf.autoTable({
            head: [['cột 1', 'cột 2', 'cột 3', 'cột 4', 'cột 5']],
            body: [body],
            startY: 50,
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
        pdf.setFontSize(15)

        pdf.text(foot, 20, pdf.lastAutoTable.finalY + 15)

        pdf.autoPrint({ variant: 'non-conform' });

        pdf.save('report.pdf')

    })

})

