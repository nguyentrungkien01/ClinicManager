// click button change password

var numberFlag = false;
var lengthFlag = false;
var titleAlert = ''
var textAlert = ''


function passAccountData() {
    fetch('/api/change_password', {
        method: 'post',
        body: JSON.stringify({
            'username': document.getElementById("username").innerText.slice('nguoi dung: '.length).trim(),
            'old_password': document.getElementById("oldPsw").value,
            'new_password': document.getElementById("newPsw").value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        console.info(res)
        return res.json()
    }).then(function (datas) {
        console.info(datas)

        if (datas['result']) {
            Swal.fire(
                'Đổi mật khẩu thành công!',
                'Mật khẩu của bạn đã được cập nhật.',
                'success'
            ).then(function () {
                window.location = '/admin/';
            })
        } else {
            Swal.fire({
                title: 'Đổi mật khẩu không thành công',
                text: 'Xin vui lòng nhập lại',
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
        }
    }).then(function (err) {
        console.info(err)
    })
}

$(document).ready(function () {
    $('#cfm').click(function () {

        var flag = checkAlertWrong()
        if (!flag) {
            Swal.fire({
                title: titleAlert,
                text: textAlert,
                icon: 'warning',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            return
        }
        Swal.fire({
            title: 'Bạn có chắc chắn đổi mật khẩu ?',
            text: 'Mọi thao tác sau khi thực hiện không thể phục hồi lại',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Xác nhận',
            cancelButtonText: 'Huỷ bỏ'
        }).then((result) => {
            if (result.isConfirmed) {
                passAccountData()
            }
        })

    })

    $('#oldPsw').onkeyup(function () {
        // Validate numbers
        if ($(this).val().match(numbers))
            numberFlag = true;

        // Validate length
        if (myInput.value.length >= 8)
            lengthFlag = true;
    })

})

function checkCondition(element, text) {
    if (!(element.val().length >= 8 && element.val().length <= 12)) {
        titleAlert = `Độ dài của ${text} không hợp lệ'`
        textAlert = 'Lưu ý: độ dài từ 8 đến 12 ký tự'
        return false
    }
    var numbers = /[0-9]/g;
    if (element.val().match(numbers) == null) {
        titleAlert = `${text} chỉ được nhập số`
        textAlert = 'Xin vui lòng nhập lại'
        return false
    }

    return true
}

function checkAlertWrong() {
    if (!checkCondition($('#oldPsw'))) {
        checkCondition($('#oldPsw'), 'Mật khẩu cũ')
 
        return false
    }

    if (!checkCondition($('#newPsw'))) {
        checkCondition($('#newPsw'), 'Mật khẩu mới')
        return false
    }

    if (!checkCondition($('#cfmNewPsw'))) {
        checkCondition($('#cfmNewPsw'), 'mật khẩu xác nhận')
        return false
    }

    if($('#newPsw').val() != $('#cfmNewPsw').val()){
        titleAlert = 'Mật khẩu mới không trùng khớp với mật khẩu xác nhận'
        return false
    }
    return true
}