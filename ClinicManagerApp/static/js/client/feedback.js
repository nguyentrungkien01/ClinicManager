function sendFeedback() {
    fetch('/api/client/send_feedback', {
        method: 'post',
        body: JSON.stringify({
            'customer_fullname': $('#customer_fullname').val(),
            'customer_email': $('#customer_email').val(),
            'feedback_subject': $('#feedback_subject').val(),
            'feedback_content': $('#feedback_content').val()
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        return res.json()
    }).then(function (datas) {
        if (datas['result']) {
            Swal.fire({
                title: 'Gửi phản hồi thành công',
                text: 'Cảm ơn bạn đã gửi phản hồi cho chúng tôi! Phản hồi của bạn sẽ góp phần giúp chúng tôi cải thiện dịch vụ của mình',
                icon: 'success',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            resetFeedbackData()
        } else {
            Swal.fire({
                title: 'Gửi phản hồi thất bại',
                text: 'Có một số sự cố xảy ra trong quá trình gửi! Vui lòng thử lại sau!',
                icon: 'error',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
        }
    })
}

function checkFeedbackData() {
    if ($('#customer_fullname').val().length <= 0) {
        alertFeedbackData('Thông tin tên khách hàng không được để trống')
        return false
    }
     if ($('#customer_fullname').val().length > 100) {
            alertFeedbackData('Thông tin tên khách hàng không được vượt quá 100 ký tự')
            return false
        }
    if ($('#customer_email').val().length <= 0) {
        alertFeedbackData('Thông tin email không được để trống')
        return false
    }

    if (!$('#customer_email').val().match(
            /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        )) {
        alertFeedbackData('Email không hợp lệ')
        return false
    }
       if ($('#customer_email').val().length >50) {
        alertFeedbackData('Thông tin email không được vượt quá 50 ký tự')
        return false
    }

    if ($('#feedback_subject').val().length <= 0) {
        alertFeedbackData('Tiêu đề phản hồi không được để trống')
        return false
    }
    if ($('#feedback_subject').val().length >200) {
        alertFeedbackData('Tiêu đề phản hồi không được vượt quá 200 ký tự')
        return false
    }
    if ($('#feedback_content').val().length <= 0) {
        alertFeedbackData('Nội dung phản hồi không được để trống')
        return false
    }
    return true
}

function alertFeedbackData(title) {
    Swal.fire({
        title: 'Cảnh báo',
        text: title,
        icon: 'error',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'Ok',
    })
}

function resetFeedbackData() {
    $('#customer_fullname').val('')
    $('#customer_email').val('')
    $('#feedback_subject').val('')
    $('#feedback_content').val('')
}

$('#feed_back_cfm').click(function () {
    if (checkFeedbackData()) {
        sendFeedback()
    }
})