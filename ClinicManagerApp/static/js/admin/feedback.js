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
        console.info(datas)
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
                <button class="page-link" onclick='setPrevious(${amountPage} )'><</button>
            </li>`
        for (let i = 1; i <= amountPage; i++)
            page += `<li class="page-item ${i == 1 ? 'active' : ''}">
                    <button class="page-link" onclick='setPage(${i},${amountPage})'>${i}</button>
                </li>`

        page += `<li class="page-item" id = 'next_item'>
                <button class="page-link" onclick='setNext(${amountPage}, ${amount})'>></button>
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
    rows=''
    for(let i =0; i<datas.length; i++){
        feedbackId = datas[i]['feedback_id']
        feedbackSubject=datas[i]['feedback_subject']
        customerName = datas[i]['customer_name']
        dateCreated= datas[i]['date_created']
        rows+=`
                <div>
                    <div onclick ='getFeedbackContent(${feedbackId})'>
                        <h1>#${feedbackId} - ${feedbackSubject}</h1>
                        <p>${customerName}</p>
                        <p>${dateCreated}</p>
                    </div>
                    <div id='feedback_content_${feedbackId}'>
                    </div>
                </div>
        `
    }

    if (datas.length > 0)
        $('#feedback_dashboard').html(rows)

}

function showFeedbackContent(datas, feedbackId){
    if($(`#feedback_content_${feedbackId}`).children().length > 0){
        $(`#feedback_content_${feedbackId}`).html('')
    }
    else{
        content=`
                    <p>${datas['content']}</p>
                    <a href='mailto:${datas['gmail']}'>Phản hồi mail</a>
        `
        document.getElementById(`feedback_content_${feedbackId}`).
            insertAdjacentHTML("beforeend", content);
    }
   
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
