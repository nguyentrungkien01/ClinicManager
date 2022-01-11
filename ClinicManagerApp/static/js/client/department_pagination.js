var gPageSize = null
var gBegIdx = null
var gEndIdx = null
var gCurrentPage = null

function getAmountDepartment() {
    fetch('/api/client/amount_department').then(function (res) {
        return res.json()
    }).then(function (datas) {
        setPagegination(parseInt(datas['amount']))
    })
}

function getInforDepartment() {
    fetch('/api/client/infor_department', {
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
        setDepartmentData(datas)
    })
}

function setPagegination(amount) {
    var page = ''
    var amountPage = Math.ceil(amount / gPageSize)
    if (amount <= gPageSize) {
        $('#pagination_service').html('')
        return
    }
    if (amountPage != 1) {
        gCurrentPage = 1
        $('#pagination_service').html('')
        page += `<li class="page-item" id ='previous_item_service'>
                <button class="page-link" onclick='setPrevious(${amountPage} )'><<</button>
            </li>`
        for (let i = 1; i <= amountPage; i++)
            page += `<li class="page-item ${i == 1 ? 'active' : ''}">
                    <button class="page-link" onclick='setPage(${i},${amountPage})'>${i}</button>
                </li>`

        page += `<li class="page-item" id = 'next_item_service'>
                <button class="page-link" onclick='setNext(${amountPage}, ${amount})'>>></button>
            </li>`
        $('#pagination_service').html(page)
    }
}

function setPrevious(amountPage) {
    if (gBegIdx - gPageSize >= 0) {
        $('#previous_item_service').show()
        gCurrentPage--
        if (gCurrentPage == 1)
            $('#previous_item_service').hide()

        if (gCurrentPage == 1 && gCurrentPage != amountPage)
            $('#next_item_service').show()

        gBegIdx -= gPageSize
        gEndIdx = gBegIdx + gPageSize
        getInforDepartment()
    } else {
        $('#previous_item_service').hide()
    }
    $('#pagination_service').children().removeClass('active')
    $(`#pagination_service li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setNext(amountPage, amountData) {
    if (gBegIdx + gPageSize <= amountData) {
        $('#next_item_service').show()
        gCurrentPage++;
        if (gCurrentPage == amountPage)
            $('#next_item_service').hide()
        if (gCurrentPage == amountPage && gCurrentPage != 1)
            $('#previous_item_service').show()

        gBegIdx += gPageSize
        gEndIdx = gBegIdx + gPageSize
        getInforDepartment()
    } else {
        $('#next_item_service').hide()
    }
    $('#pagination_service').children().removeClass('active')
    $(`#pagination_service li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setPage(itemIdx, amountPage) {
    gCurrentPage = itemIdx
    if (itemIdx == amountPage) {
        $('#next_item_service').hide()
        if (itemIdx != 1)
            $('#previous_item_service').show()
    } else
    if (itemIdx == 1) {
        $('#previous_item_service').hide()
        if (itemIdx != amountPage)
            $('#next_item_service').show()
    } else {
        $('#previous_item_service').show()
        $('#next_item_service').show()
    }

    gBegIdx = (itemIdx - 1) * gPageSize
    gEndIdx = gBegIdx + gPageSize
    getInforDepartment()
    $('#pagination_service').children().removeClass('active')
    $(`#pagination_service li:nth-child(${gCurrentPage + 1})`).addClass('active')
}

function setIndexPagination() {
    gBegIdx = 0
    gEndIdx = gBegIdx + gPageSize
}

function setDepartmentData(datas) {
    if (datas == undefined)
        return
    $('#department_info').html('')
    cols = ''
    for (let i = 0; i < datas.length; i++) {
        department_logo = datas[i]['department_logo']
        department_name = datas[i]['department_name']
        department_description = datas[i]['department_description']
        if (department_logo == null)
            department_logo = 'https://res.cloudinary.com/ouproject/image/upload/v1641740695/department_logo/default_logo_gt7ejd.png'
        if (department_description == null)
            department_description = ''
        cols += `
                <div class="d-flex col-lg-3 col-md-6 col-sm-6 col-12">
                    <div class="hc-service-box">
                        <div class="hc-service-icon hc-service-ico-clr1">
                            <img src="${department_logo}" alt="service" />
                        </div>
                            <h1 class="hc-service-title">${department_name}</h1>
                            <p>${department_description}</p>
                            <a href="javascript:;" class="hc-service-arrow">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 493.356 493.356">
                                    <path
                                        d="M490.498,239.278l-109.632-99.929c-3.046-2.474-6.376-2.95-9.993-1.427c-3.613,1.525-5.427,4.283-5.427,8.282v63.954H9.136
                                        c-2.666,0-4.856,0.855-6.567,2.568C0.859,214.438,0,216.628,0,219.292v54.816c0,2.663,0.855,4.853,2.568,6.563
                                        c1.715,1.712,3.905,2.567,6.567,2.567h356.313v63.953c0,3.812,1.817,6.57,5.428,8.278c3.62,1.529,6.95,0.951,9.996-1.708
                                        l109.632-101.077c1.903-1.902,2.852-4.182,2.852-6.849C493.356,243.367,492.401,241.181,490.498,239.278z" />
                                </svg>
                            </a>
                        </div>
                    </div>`
    }
    if (datas.length > 0)
        $('#department_infor').html(cols)
}

function initData() {
    gPageSize = 4
    setIndexPagination()
    getAmountDepartment()
    getInforDepartment()
}

initData()