var gPageSize = null
var gBegIdx = null
var gEndIdx = null
var gCurrentPage = null


function getAmountFeedback() {
    fetch('/api/admin/feedback_amount').then(function (res) {
        return res.json()
    }).then(function (datas) {
        setPagegination(parseInt(datas['amount']))
    })
}

function getGeneralFeedbackInfor() {
    fetch('/api/admin/general_feedback_infor', {
        method: 'post',
        body: JSON.stringify({
            'begin_index': gBegIdx,
            'end_index': gEndIdx
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setGeneralFeedbackData(datas)
    })
}

function getFeedbackContent(feedbackId = None) {
    fetch('/api/admin/feedback_content', {
        method: 'post',
        body: JSON.stringify({
            'feedback_id': feedbackId
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        //show feedback content
        showFeedbackContent(datas, feedbackId)
    })
}

function setPagegination(amount) {
    var page = ''
    var amountPage = Math.ceil(amount / gPageSize)
    if (amount <= gPageSize) {
        $('#pagination').html('')
        return
    }
    if (amountPage != 1) {
        gCurrentPage = 1
        $('#pagination').html('')
        page += `<li class="page-item" id ='previous_item'>
                <button class="page-link" onclick='setPrevious(${amountPage} )'><<</button>
            </li>`
        for (let i = 1; i <= amountPage; i++)
            page += `<li class="page-item ${i == 1 ? 'active' : ''}">
                    <button class="page-link" onclick='setPage(${i},${amountPage})'>${i}</button>
                </li>`

        page += `<li class="page-item" id = 'next_item'>
                <button class="page-link" onclick='setNext(${amountPage}, ${amount})'>>></button>
            </li>`
        $('#pagination').html(page)
    }
}

function setPrevious(amountPage) {
    if (gBegIdx - gPageSize >= 0) {
        $('#previous_item').show()
        gCurrentPage--
        if (gCurrentPage == 1)
            $('#previous_item').hide()

        if (gCurrentPage == 1 && gCurrentPage != amountPage)
            $('#next_item').show()

        gBegIdx -= gPageSize
        gEndIdx = gBegIdx + gPageSize
        getGeneralFeedbackInfor()
    } else {
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
        getGeneralFeedbackInfor()
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
    } else
    if (itemIdx == 1) {
        $('#previous_item').hide()
        if (itemIdx != amountPage)
            $('#next_item').show()

    } else {
        $('#previous_item').show()
        $('#next_item').show()
    }
    gBegIdx = (itemIdx - 1) * gPageSize
    gEndIdx = gBegIdx + gPageSize
    getGeneralFeedbackInfor()
    $('#pagination').children().removeClass('active')
    $(`#pagination li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setIndexPagination() {
    gBegIdx = 0
    gEndIdx = gBegIdx + gPageSize
}

function setGeneralFeedbackData(datas) {
    if (datas == undefined)
        return
    $('#feedback_dashboard').html('')
    rows = ''
    for (let i = 0; i < datas.length; i++) {
        feedbackId = datas[i]['feedback_id']
        feedbackSubject = datas[i]['feedback_subject']
        customerName = datas[i]['customer_name']
        dateCreated = datas[i]['date_created']
        rows += `
                <div class="row">
                    <div class="col-12 col-lg-5">
                        <div>
                        <h3 class="font-weight-bold">#${feedbackId}</h3>
                        <h4 class="font-weight-bold"><span class="text-success">Tiêu đề:</span> ${feedbackSubject}</h4>
                        <h5>Người gửi: ${customerName}</h5>
                        <h5>Ngày gửi: ${dateCreated}</h5>
                        </div>
                    </div>
                    <div class="col-12 col-lg-7">
                        <div class="accordion accordion-secondary">
                            <div class="card">
                                <div class="card-header collapsed" id="headingOne" data-toggle="collapse"
                                    data-target="#feedback${feedbackId}" aria-expanded="true"
                                    aria-controls="feedback${feedbackId}" role="button" onclick ='getFeedbackContent(${feedbackId})'>
                                    <div class="span-icon"><i class="fas fa-th-large"></i></div>
                                    <div class="span-title">Nội dung</div>
                                    <div class="span-mode"></div>
                                </div>
                                <div id="feedback${feedbackId}" class="collapse">
                                    <div class="card-body" id='feedback_content_${feedbackId}'>
                                    <p id="feedback_content${feedbackId}"></p>
                                    <a class="btn btn-secondary" id="mail_reply${feedbackId}">Phản hồi mail</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="separator-dashed"></div>
        `
    }
    if (datas.length > 0)
        $('#feedback_dashboard').html(rows)
}

function showFeedbackContent(datas, feedbackId) {
    $(`#feedback_content${feedbackId}`).text(datas['content'])
    $(`#mail_reply${feedbackId}`).attr("href", `mailto:${datas['gmail']}`)
}

function initData() {
    gPageSize = 10
    setIndexPagination()
    getAmountFeedback()
    getGeneralFeedbackInfor()
}

$(document).ready(function () {
    initData()
})