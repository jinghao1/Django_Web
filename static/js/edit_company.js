

 

// 文本编辑器
$(function () {
    // window.ue 是将ue这个变量作为全局变量来定义
    window.ue = UE.getEditor('editor',{
        // 官方文档中给出前端的高度配置说明
        "initialFrameHeight":400 , //初始化编辑器宽度
        'serverUrl':'/ueditor/upload/' // 服务器统一请求接口路径
    });
});

// 更新企业信息
$(function () {
    var submiBtn = $('#submit-btn');
    submiBtn.click(function (event) {
        event.preventDefault(); // 去除原有的格式
        var btn = $(this); // 当前点击的这个按钮
        var fullName = $("input[name='fullName']").val();
        var legalPersonName = $("input[name='legalPersonName']").val();
        var businessScope = $("#businessScope").val();
        var phone = $("input[name='phone']").val();
        var email = $("input[name='email']").val();
        var address = $("input[name='address']").val();
        var company_url = $("input[name='company_url']").val();
        var desc = $("#desc_info_desc").val();
    
        var code = $("input[name='code']").val();
        var lang = $("input[name='lang']").val();
      
        var gs_info_id = btn.attr('data-gs_info-id'); 
        var url = '/cms/company_edit/';
        // console.log(businessScope)
        xfzajax.post({
            'url':url,
            'data': {
                'fullName':fullName,
                'lang':lang, 
                'legalPersonName':legalPersonName,
                'businessScope':businessScope,
                'desc':desc,
                'phone':phone,
                'email':email,
                'address':address,
                'company_url':company_url,
                'code':code,
                'pk':gs_info_id
            },

            'success':function (result) {
                if (result['code'] === 200){

                    xfzalert.alertSuccess('企业信息已更新！',function () {
                        url = '/cms/company_list/';
                        window.location.reload(); // 重新加载当前界面

                    });
                }
            }
        });
    });
});

