var _hmt = _hmt || [];

(function () {
    $("a[href*='www.t00ls.net']").click(function (event) {
        event.preventDefault();
        var content = $(event.target).attr("href");
        const input = document.createElement('input');
        input.setAttribute('readonly', 'readonly');
        input.setAttribute('value', content);
        document.body.appendChild(input);
        input.select();
        if (document.execCommand('copy')) {
            document.execCommand('copy');
            $.notify("<strong>T00ls.net</strong> 不允许从外链打开，地址已经复制到剪切板，享受吧~", {
                type: 'success',
                delay: 2000,
                allow_dismiss: false,
                placement: {
                    align: "center"
                }

            });
        }
        document.body.removeChild(input);
    });
    var host = window.location.hostname;
    var site = "i.hacking8.com";
//    if ((host !== site) && (host !== '127.0.0.1')) {
//        location.href = 'https://i.hacking8.com';
//    }
    $(".main .media .tags a").click(function (event) {
        event.preventDefault();
        var content = $(event.target).attr("href");
        $.ajax({
            url: content, success: function (result) {
                if (result.status === "ok") {
                    $.notify("谢谢主人打的标签～刷新后显示哦", {
                        type: 'success',
                        delay: 2000,
                        allow_dismiss: false,
                        placement: {
                            align: "center"
                        }
                    });
                }
                else {
                    $.notify("可能出现了一些错误哦", {
                        type: 'error',
                        delay: 2000,
                        allow_dismiss: false,
                        placement: {
                            align: "center"
                        }
                    });
                }
            }
        });
    });
    $(".media .star-option a").click(function (event) {
        event.preventDefault();
        var title = $(this).parents(".media").find(".link a").text();
        var action = $(event.target).attr("href");
        $('#starModal form').attr("action", action);
        $('#starModal form .title span').text(title);
        $('#starModal').modal('toggle');
    });

    $('[data-toggle="popover"]').each(function(event){
        let key = $(this).attr("data-key");
        $(this).popover({
            html:true,
            trigger: 'focus',
            content:"<div class='emoji-popover'><a href='"+key+"'></a><ul><li>👍</li><li>👎</li><li>😄</li><li>🎉</li><li>😕</li><li>❤️</li><li>🚀️</li><li>👀</li></ul></div>",
        });
    });
      $(document).on('click','.emoji-popover ul li',function(){
        let index = $(this).index();
        $('[data-toggle="popover"]').popover('hide')
        let pid = $(this).parents("div.emoji-popover").find("a").attr("href");
        console.log(index,pid);
        let url = "/api/emoji";
        $.ajax({
            url: url,
            type: "get",
              data: {
                index:index,
                pid:pid
              },
            success: function (result) {
                $.notify(result.msg, {
                    type: 'info',
                    delay: 2000,
                    allow_dismiss: false,
                    placement: {
                        align: "center"
                    }
                });
            }
        });
  });

})();