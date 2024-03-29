/* auth的注册功能部分 */

//实现图片验证码自动更新功能
//原理：设置功能每次获取imaCapacha函数刷新一次就会产生一个新的图形验证码。
// 这里利用src标签的内容一旦更改，图形验证码就会更新的原理。
// 使用JS写一个函数利用account/img_captcha/随机数的方式进行更新路由，产生新的验证码
$(function () {
  
    var imgCaptcha = $('.img-captcha');
  
    imgCaptcha.click(function () { 
        imgCaptcha.attr("src",'/account/img_captcha/'+"?random="+Math.random());
    });
});

// // 点击发送短信验证码
// $(function () {
//     var smsCaptcha = $('.sms-captcha-btn');
//     function send_sms() {
//         // var telephone = $('input[name="telephone"]');
//         // console.log('测试...');
//         var telephone = $('input[name="telephone"]').val();
//         // var telephone=document.getElementById("test");
//         //ajax请求，发送短信验证码
//         $.get({
//             'url': '/account/sms_captcha/',
//             'telephone': telephone,
//             'data':{'telephone':telephone},
//             'success': function (result) {
//                 var count = 60; // 短信验证码倒计时时间定义
//                 smsCaptcha.addClass('disabled');
//                 smsCaptcha.unbind('click');
//                 var timer = setInterval(function () {
//                     smsCaptcha.text(count);
//                     count--;
//                     if (count <= 0){
//                         //清除计时器
//                         clearInterval(timer);
//                         smsCaptcha.text('发送验证码');
//                         smsCaptcha.removeClass('disabled');
//                         smsCaptcha.click(send_sms);
//                     }
//                 },1000)
//             },
//             'fail': function (error) {
//                 console.log(error);
//             }
//         });
//     }
//     smsCaptcha.click(send_sms); // 当点击发送验证码时，调用send_sms函数
// });

// 注册功能
$(function () {
    var telephoneInput = $("input[name='telephone']");
    var usernameInput = $("input[name='username']");
    var imgCaptchaInput = $("input[name='img_captcha']");
    var company_nameInput = $("input[name='company_name']");
    var hangyeInput = $("input[name='hangye']");
    var rongziInput = $("input[name='rongzi']");
    var otherInput = $("input[name='other']");
    var smsCaptchaInput = $("input[name='sms_captcha']");
    var submitBtn = $(".submit-btn-pro");

    submitBtn.click(function (event) {
  
        event.preventDefault();
        var telephone = telephoneInput.val();
        var username = usernameInput.val();
        var imgcaptcha = imgCaptchaInput.val();
        var company_name = company_nameInput.val();
        var hangye = hangyeInput.val();
        var rongzi = rongziInput.val();
        var other = otherInput.val();
        // var smscaptcha = smsCaptchaInput.val();

        if(!telephone || telephone.length !== 11){
            alert('手机号码输入不正确！');
            return;
        }

        xfzajax.post({
            'url': '/account/project_register/',
            'data':{
                'telephone':telephone,
                'username':username,
                'company_name':company_name,
                'hangye':hangye,
                'img_captcha':imgcaptcha,
                'rongzi':rongzi,
                'other':other
                // 'sms_captcha':smscaptcha
            },
            'success':function (result) {
                if(result['code'] === 200){
                    alert("success");
                    window.location = '/';
                }else{
                    //使用message文件的方式将所有错误信息进行返回,相比直接使用js的alert会好看实用写
                    var message = result['message'];
                    // window.messageBox.showError(message);
                    // 使用js自带的弹框alert
                    alert(result['message']);
                }
            },
            'fail':function (error) {
                console.log(error);
            }
        });
    });

});
