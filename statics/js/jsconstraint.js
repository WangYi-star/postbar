function verify() {
    var reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~@#$%\*-\+=:,\\?\[\]\{}]).{8,16}$/;
    var password = document.getElementById("password").value;
    var uid = document.getElementById("uid").value;
    if(!uid)
        alert("请输入用户ID！！！");
    else{
        if(!password)
            alert("请输入密码！！！");
        else{
            if (reg.test(password)){
                var form = document.getElementById("register_form");
                form.submit();
            }
            else{
                alert("密码不匹配，请重新输入！！！")
            }
        }
    }
}