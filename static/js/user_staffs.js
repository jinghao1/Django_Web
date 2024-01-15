
// 删除用户
$(function () {
    var deleteBtnUser = $('.delete-btn-user');
    deleteBtnUser.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        xfzalert.alertConfirm({
            'text':'你确认要删除该用户吗？',
            // 如果用户点击了确认，执行后面的操作
            'confirmCallback':function () {
                console.log('删除ajax请求开始');
                // 执行Ajax请求
                xfzajax.post({
                    'url':'/cms/delete_staff/',
                    'data':{
                      'pk':pk
                    },
                    // 如果成功则执行下面操作
                    'success':function (result) {
                        console.log(result);
                        if (result['code'] === 200){
                            // 重新加载页面
                            window.location.reload();
                        }
                    }
                });
            }
        });
    })
});
