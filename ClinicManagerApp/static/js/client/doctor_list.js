var gPageSizeDoctor = null
var gBegIdxDoctor = null
var gEndIdxDoctor = null
var gCurrentPageDoctor = null
var gCurrentTabId = null

function getMajor() {
    fetch('/api/client/major_doctor').then(function (res) {
        return res.json()
    }).then(function (datas) {
        setMajorList(datas)
    })
}

function getAmountDoctor(tab_id = null) {
    major_id = null
    if (tab_id != null)
        major_id = tab_id
    gCurrentTabId = tab_id
    fetch('/api/client/amount_doctor', {
        method: 'post',
        body: JSON.stringify({
            'major_id': major_id
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setPageginationDoctor(parseInt(datas['amount']))
    })
}

function getInforDoctor(tab_id = null, isReset = false) {
    if (tab_id == 0)
        tab_id = null
    major_id = null
    if (tab_id != null)
        major_id = tab_id
    gCurrentTabId = tab_id

    if (isReset) {
        setIndexPaginationDoctor()
        getAmountDoctor(tab_id = tab_id)
        $('#major_list li a').removeClass('hc-team-tab-active')
        $(`#major_list li:nth-child(${major_id + 1}) a`).addClass('hc-team-tab-active')
    }

    fetch('/api/client/doctor_list', {
        method: 'post',
        body: JSON.stringify({
            'major_id': major_id,
            'begin_index': gBegIdxDoctor,
            'end_index': gEndIdxDoctor
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        setDoctorData(datas)
    })
}

function setMajorList(datas) {
    $('#major_list').html('')
    cols = `<li>
                <a class="hc-team-tab-active" 
                    onclick ="getInforDoctor(tab_id=${0}, isReset=true)">Tất cả</a>
            </li>`
    for (let i = 0; i < datas.length; i++)
        cols += `<li>
                <a onclick ="getInforDoctor(tab_id=${datas[i]['major_id']}, isReset=true)">${datas[i]['major_name']}</a>
                </li>`
    $('#major_list').html(cols)
}

function setPageginationDoctor(amount) {
    var page = ''
    var amountPage = Math.ceil(amount / gPageSizeDoctor)
    if (amount <= gPageSizeDoctor) {
        $('#pagination_doctor').html('')
        return
    }
    if (amountPage != 1) {
        gCurrentPageDoctor = 1
        $('#pagination_doctor').html('')
        page += `<li class="page-item" id ='previous_item_doctor'>
                <button class="page-link" onclick='setPreviousDoctor(${amountPage} )'><<</button>
            </li>`
        for (let i = 1; i <= amountPage; i++)
            page += `<li class="page-item ${i == 1 ? 'active' : ''}">
                    <button class="page-link" onclick='setPageDoctor(${i},${amountPage})'>${i}</button>
                </li>`

        page += `<li class="page-item" id = 'next_item_doctor'>
                <button class="page-link" onclick='setNextDoctor(${amountPage}, ${amount})'>>></button>
            </li>`
        $('#pagination_doctor').html(page)
    }
}

function setPreviousDoctor(amountPage) {
    if (gBegIdxDoctor - gPageSizeDoctor >= 0) {
        $('#previous_item_doctor').show()
        gCurrentPageDoctor--
        if (gCurrentPageDoctor == 1)
            $('#previous_item_doctor').hide()

        if (gCurrentPageDoctor == 1 && gCurrentPageDoctor != amountPage)
            $('#next_item_doctor').show()


        gBegIdxDoctor -= gPageSizeDoctor
        gEndIdxDoctor = gBegIdxDoctor + gPageSizeDoctor
        getInforDoctor(tab_id = gCurrentTabId)
    } else {
        $('#previous_item_doctor').hide()
    }

    $('#pagination_doctor').children().removeClass('active')
    $(`#pagination_doctor li:nth-child(${gCurrentPageDoctor + 1})`).addClass('active')
}

function setNextDoctor(amountPage, amountData) {
    if (gBegIdxDoctor + gPageSizeDoctor <= amountData) {
        $('#next_item_doctor').show()
        gCurrentPageDoctor++;
        if (gCurrentPageDoctor == amountPage)
            $('#next_item_doctor').hide()
        if (gCurrentPageDoctor == amountPage && gCurrentPageDoctor != 1)
            $('#previous_item_doctor').show()

        gBegIdxDoctor += gPageSizeDoctor
        gEndIdxDoctor = gBegIdxDoctor + gPageSizeDoctor
        getInforDoctor(tab_id = gCurrentTabId)
    } else {
        $('#next_item_doctor').hide()
    }

    $('#pagination_doctor').children().removeClass('active')
    $(`#pagination_doctor li:nth-child(${gCurrentPageDoctor + 1})`).addClass('active')
}

function setPageDoctor(itemIdx, amountPage) {
    gCurrentPageDoctor = itemIdx
    if (itemIdx == amountPage) {
        $('#next_item_doctor').hide()
        if (itemIdx != 1)
            $('#previous_item_doctor').show()
    } else
    if (itemIdx == 1) {
        $('#previous_item_doctor').hide()
        if (itemIdx != amountPage)
            $('#next_item_doctor').show()
    } else {
        $('#previous_item_doctor').show()
        $('#next_item_doctor').show()
    }

    gBegIdxDoctor = (itemIdx - 1) * gPageSizeDoctor
    gEndIdxDoctor = gBegIdxDoctor + gPageSizeDoctor
    getInforDoctor(tab_id = gCurrentTabId)
    $('#pagination_doctor').children().removeClass('active')
    $(`#pagination_doctor li:nth-child(${gCurrentPageDoctor + 1})`).addClass('active')
}

function setIndexPaginationDoctor() {
    gBegIdxDoctor = 0
    gEndIdxDoctor = gBegIdxDoctor + gPageSizeDoctor
}

function setDoctorData(datas) {
    if (datas == undefined)
        return
    $('#doctor_list').html('')
    cols = ''
    for (let i = 0; i < datas.length; i++) {
        avatar = datas[i]['avatar']
        fullname = datas[i]['full_name']
        major = datas[i]['major']
        department = datas[i]['department']
        phoneNumber = datas[i]['phone_number']
        facebookLink = datas[i]['facebook_link']
        twitterLink = datas[i]['twitter_link']
        if (avatar == null)
            avatar = 'https://res.cloudinary.com/ouproject/image/upload/v1641740748/avatar_staff/default_avatar_mvuqgu_g1nu1d.png'

        if (department == null)
            department = ''

        if (facebookLink == null)
            facebookLink = ''
        if (twitterLink == null)
            twitterLink = ''
        cols += `
                <div class="d-flex col-lg-4 col-md-6 col-sm-6 col-12">
                <div class="hc-team-box">
                    <span class="hc-dr-rating"><i class="fas fa-star"></i> 4.5</span>
                <div class="hc-team-img">
                    <img src="${avatar}" alt="team" />
                </div>
                    <h1 class="hc-team-name">Dr. ${fullname}</h1>
                    <h2 class="hc-team-designation">${major}</h2>
                    <p>${department}</p>
                <ul class="hc-team-social">
                    <li>
                        <a href="${facebookLink}"><i class="fab fa-facebook-f"></i></a>
                    </li>
                    <li>
                        <a href="${twitterLink}"><i class="fab fa-twitter"></i></a>
                    </li>
                    <li>
                        <a href="tel:${phoneNumber}"><i class="fas fa-phone-alt"></i></a>
                    </li>
                </ul>
                </div>
            </div>`
    }
    $('#doctor_list').html(cols)
}

function initDataDoctor() {
    gPageSizeDoctor = 6
    getMajor()
    setIndexPaginationDoctor()
    getAmountDoctor()
    getInforDoctor()
}
$(document).ready(function () {
    initDataDoctor()
})