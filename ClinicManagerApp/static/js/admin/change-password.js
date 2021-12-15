// click button change password
var myInput = document.getElementById("psw");
var letterFlag = false;
var capitalFlag = false;
var numberFlag = false;
var lengthFlag = false;

// When the user starts to type something inside the password field
myInput.onkeyup = function () {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters))
        letterFlag = true;

    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters))
        capitalFlag = true;

    // Validate numbers
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers))
        numberFlag = true;

    // Validate length
    if (myInput.value.length >= 8)
        lengthFlag = true;
}


function changePass() {
    if (letterFlag && capitalFlag && numberFlag && lengthFlag) {
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
                Swal.fire(
                    'Đổi mật khẩu thành công!',
                    'Mật khẩu của bạn đã được cập nhật.',
                    'success'
                ).then(function () {
                    window.location = 'http://127.0.0.1:5000/admin/';
                })
            }
        })
    } else {
        Swal.fire({
            title: 'Bạn chưa nhập đủ hoặc sai thông tin !',
            text: 'Xin vui lòng nhập đầy đủ thông tin',
            icon: 'warning',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Ok',
        })
    }
}