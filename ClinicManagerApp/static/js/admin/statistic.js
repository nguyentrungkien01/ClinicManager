var gChart = null
var gType = null
var gData = null
var gLabels = null
var gFromTime = null
var gToTime = null
var gFlagInputTime = null
var gBgChart = null
var gIndexHint = null

function getNameMedicine() {
    fetch('/api/admin/name_medicine', {
        method: 'post',
        body: JSON.stringify({
            'name_medicine': $('#name_medicine').val() == undefined ? null : $('#name_medicine').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        if (datas.length > 0)
            gIndexHint = 1
        var row = ''
        for (let i = 0; i < datas.length; i++) {
            row += `<p onclick = "onClickHint('${datas[i]['value']}')"
            onmouseover="onMouseOverHint(${i + 1})">
                ${datas[i]['value']}</p>`
        }
        document.getElementById('result_input_name').innerHTML = row
    })
}

function getData() {
    var data = $('#name_medicine').val()
    if (data == undefined || data.length <= 0)
        data = null
    else
        data = $('#name_medicine').val()

    fetch('/api/admin/statistic', {
        method: 'post',
        body: JSON.stringify({
            'statistic_type': $('#statistic_type').val(),
            'name_medicine': data,
            'statistic_condition': $('#statistic_condition').val(),
            'from_time': gFromTime,
            'to_time': gToTime
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setInputStatistic()
        if (datas.length <= 0) {
            resetData()
            return
        }
        $('#pdfChart').show()
        $('#statistic_table').show()

        loadDataTable(datas)
        loadData(datas)
        createChart(type = gType,
            label = $("#statistic_type option:selected").text(),
            data = gData,
            labels = gLabels)

    })
}

function onClickHint(hint) {
    $('#name_medicine').val(hint.trim())
    $('#result_input_name').html('')
    getData()
}

function onMouseOverHint(position) {
    gIndexHint = position
    for (let i = 1; i <= $('#result_input_name').children().length; i++)
        $(`.stats-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
    $(`.stats-choice .show-hint p:nth-child(${position})`).css("background-color", "#04a9f5");

}

function init() {
    gType = 'pie'
    gData = gLabels = []
    gFlagInputTime = false
    getData()
}

function resetData() {
    gData = []
    gChart.destroy()
    $('#pdfChart').hide()
    $('#statistic_table').hide()
}

function setInputStatistic() {
    var conditionSelect = document.getElementById('statistic_condition').value
    var inputTimeArea = document.getElementById('input_time')

    inputTimeArea.style.display = "none"
    if (conditionSelect.indexOf('month') != conditionSelect.lastIndexOf('month') ||
        conditionSelect.indexOf('quarter') != conditionSelect.lastIndexOf('quarter') ||
        conditionSelect.indexOf('year') != conditionSelect.lastIndexOf('year')) {
        var minVal = null
        var maxVal = null
        if (conditionSelect.includes('month')) {
            minVal = 1
            maxVal = 12
        }
        if (conditionSelect.includes('quarter')) {
            minVal = 1
            maxVal = 4
        }
        if (conditionSelect.includes('year')) {
            minVal = 2021
            maxVal = 2100
        }
        inputTimeArea.style.display = "flex"
        var leftInput = document.getElementById('left_time')
        var rightInput = document.getElementById('right_time')
        var selection = ''
        for (let i = minVal; i <= maxVal; i++)
            selection += `<option value=${i}>${i}</option>`

        if (!gFlagInputTime) {
            leftInput.innerHTML = selection
            rightInput.innerHTML = selection
            gFlagInputTime = true
            gFromTime = gToTime = minVal
            getData()
        }
    }
}

function setLabelHeaderTable() {
    var conditionSelect = document.getElementById("statistic_condition").value
    if (conditionSelect.includes('month'))
        return "Tháng"
    if (conditionSelect.includes('quarter'))
        return "Quý"
    return "Năm"
}

function setResultHeaderTable() {
    var type_select = document.getElementById("statistic_type").value
    if (type_select.includes('revenue'))
        return "Tổng doanh thu"
    if (type_select.includes('examination'))
        return "Tần suất khám bệnh"
    return "Tần suất sử dụng thuốc"

}

// load data of data table
function loadDataTable(datas) {
    var row = ""
    var header = `<tr>
                    <th>${'Số thứ tự'}</th>
                    <th>${setLabelHeaderTable()}</th>
                    <th>${setResultHeaderTable()}</th>
                </tr>`

    for (let i = 0; i < datas.length; i++)
        if (!$('#statistic_type').val().includes('revenue'))
            row += `<tr> 
                    <td>${i + 1}</td>
                    <td>${datas[i]['key']}</td>
                    <td>${datas[i]['value'].substring(0, datas[i]['value'].indexOf(' ')).replaceAll(',','')}</td>
                </tr>`
        else
            row += `<tr> 
                    <td>${i + 1}</td>
                    <td>${datas[i]['key']}</td>
                    <td>${datas[i]['value']}</td>
                </tr>`

    document.getElementById('title_statistic_table').innerHTML = header;
    document.getElementById('data_statistic_table').innerHTML = row;
}

// load data for chart
function loadData(datas) {
    gData = [];
    gLabels = [];
    for (let i = 0; i < datas.length; i++) {
        gLabels.push(datas[i]['key']);
        gData.push(parseInt(datas[i]['value']));
    }

}

//change data of chart
$(document).ready(function () {
    gBgChart = $('.card').css('background-color')

    $('#name_medicine').keydown(function (event) {
        if (gIndexHint == null)
            return;
        if (event.keyCode == 13) {
            event.preventDefault()
            $('#name_medicine').val($(`.stats-choice .show-hint p:nth-child(${gIndexHint})`).text().trim())
            $('#result_input_name').html('')
            getData()
        }

        if (event.keyCode == 40) {
            for (let i = 1; i <= $('#result_input_name').children().length; i++)
                $(`.stats-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (++gIndexHint > $('#result_input_name').children().length)
                gIndexHint = 1
            $(`.stats-choice .show-hint p:nth-child(${gIndexHint})`).css("background-color", "#04a9f5");

        }
        if (event.keyCode == 38) {
            for (let i = 1; i <= $('#result_input_name').children().length; i++)
                $(`.stats-choice .show-hint p:nth-child(${i})`).css("background-color", "white");
            if (--gIndexHint <= 0)
                gIndexHint = $('#result_input_name').children().length
            $(`.stats-choice .show-hint p:nth-child(${gIndexHint})`).css("background-color", "#04a9f5");

        }
    })

    // check theme color when user refesh page
    window.onload = function () {
        if ($("body").attr('data-background-color') == 'bg1')
            gBgChart = '#ffffff';
        else if ($("body").attr('data-background-color') == 'bg2')
            gBgChart = '#ffffff';
        else if ($("body").attr('data-background-color') == 'bg3')
            gBgChart = '#ffffff';
        else
            gBgChart = '#202940';

        createChart(type = gType,
            label = $("#statistic_type option:selected").text(),
            data = gData,
            labels = gLabels)
    };
    // check theme color when user click change bg
    $('.changeBackgroundColor').click(function () {
        if ($("body").attr('data-background-color') == 'bg1')
            gBgChart = '#ffffff';
        else if ($("body").attr('data-background-color') == 'bg2')
            gBgChart = '#ffffff';
        else if ($("body").attr('data-background-color') == 'bg3')
            gBgChart = '#ffffff';
        else
            gBgChart = '#202940';

        createChart(type = gType,
            label = $("#statistic_type option:selected").text(),
            data = gData,
            labels = gLabels)
    })

    init()
    $('#input_time').hide()
    $('#input_name_medicine').hide()

    $('#name_medicine').on('input', function () {
        getNameMedicine()
        getData()
    })

    $('#name_medicine').focus(function () {
        $('#result_input_name').show()
        if (gIndexHint != null)
            $(`.stats-choice .show-hint p:nth-child(1)`).css("background-color", "#04a9f5");

    })
    $("#statistic_type").change(function () {

        getData();
        if ($(this).val() == 'frequency_of_medicine_use') {
            $('#input_name_medicine').show()

        } else {
            $('#input_name_medicine').hide()
            $('#name_medicine').val('')
            $('#result_input_name').html('')
        }


    });

    $("#chart_type").change(function () {
        gType = $(this).val();
        getData();
    });

    $("#statistic_condition").change(function () {
        gFlagInputTime = false
        if ($(this).val().indexOf('month') != $(this).val().lastIndexOf('month') ||
            $(this).val().indexOf('quarter') != $(this).val().lastIndexOf('quarter') ||
            $(this).val().indexOf('year') != $(this).val().lastIndexOf('year')) {
            gFromTime = parseInt(document.getElementById('left_time').value)
            gToTime = parseInt(document.getElementById('right_time').value)
        } else {
            gFromTime = null
            gToTime = null

        }

        getData()


    });
    $('#left_time').data('lastSelectedIndex', 0);

    $('#left_time').click(function () {
        $(this).data('lastSelectedIndex', this.selectedIndex)
    });
    $('#right_time').data('lastSelectedIndex', 0);

    $('#right_time').click(function () {
        $(this).data('lastSelectedIndex', this.selectedIndex)
    });


    $('#left_time').change(function () {
        if (parseInt($(this).val()) > parseInt($('#right_time').val())) {
            this.selectedIndex = $(this).data('lastSelectedIndex')
        } else {
            gFromTime = parseInt($(this).val())
            getData()
        }
    });
    $('#right_time').change(function () {
        if (parseInt($(this).val()) < parseInt($('#left_time').val())) {
            this.selectedIndex = $(this).data('lastSelectedIndex')
        } else {
            gToTime = parseInt($(this).val())

            getData()
        }
    });
    $('#pdfChart').click(function () {

        const canvas = document.getElementById('chart')
        canvas.toDataURL('image/jpeg', 1.0)

        const pdf = new jsPDF({
            orientation: 'portrait',
            format: 'a4',
            putOnlyUsedFonts: true,
            floatPrecision: 16
        })
        pdf.setFontSize(13)

        pdf.addImage({
            imageData: canvas,
            format: 'JPEG',
            x: 5,
            y: 15,
            width: 250,
            height: 200
        })
        pdf.addPage({
            format: 'a4',
            orientation: 'portrait'
        })
        pdf.autoTable({
            html: '#statistic_table',
            theme: 'grid',
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
        pdf.text('@CopyRight: Open University', 77, pdf.lastAutoTable.finalY + 5)

        pdf.autoPrint({
            variant: 'non-conform'
        });
        pdf.save('statistic.pdf')
    })
});
//create chart
function createChart(type = 'pie', label = '', data = [], labels = []) {
    var backgroundColor = [];
    var borderColor = [];
    for (let i = 0; i < data.length; i++) {
        r = Math.floor(Math.random() * 255 + 1);
        g = Math.floor(Math.random() * 255 + 1);
        b = Math.floor(Math.random() * 255 + 1);
        backgroundColor.push(`rgba(${r},${g}, ${b}, 0.7)`);
        borderColor.push(`rgba(${r},${g}, ${b}, 1)`);
    }
    const ctx = document.getElementById('chart').getContext('2d');

    if (gChart != null)
        gChart.destroy();

    const bgColorPDF = {
        id: 'bgColorPDF',
        beforeDraw: (chart) => {
            const {
                ctx,
                width,
                height
            } = chart
            ctx.fillStyle = gBgChart
            ctx.fillRect(0, 0, width, height)
            ctx.restore()
        }
    }
    gChart = new Chart(ctx, {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
        plugins: [bgColorPDF]
    });
}