// click button change password

var numberFlag = false;
var lengthFlag = false;
var titleAlert = ''
var textAlert = ''


function passAccountData() {
    fetch('/api/change_password', {
        method: 'post',
        body: JSON.stringify({
            'username': document.getElementById("username").innerText,
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
                title: 'Doi mat khau khong thanh cong',
                text: 'Xin vui lòng nhập thu lai lan nua',
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
        titleAlert = `'Chieu dai cua ${text} khong hop le '`
        textAlert = 'Thong bao nhap lai'
        return false
    }
    var numbers = '/[0-9]/g';
    if (!element.val().match(numbers)) {
        titleAlert = `'${text} chi duoc nhap so'`
        textAlert = 'Nhap lai thong tin'
        return false
    }

    return true
}

function checkAlertWrong() {
    if (!checkCondition($('#oldPsw'))) {
        checkCondition($('#oldPsw'), 'Mat khau cu')
        return false
    }

    if (!checkCondition($('#newPsw')))
        return false

    if (!checkCondition($('#cfmPsw')))
        return false
    return true
}
