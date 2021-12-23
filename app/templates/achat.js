$(function () {

    $("#filters :checkbox").click(function () {

        var re = new RegExp($("#filters :checkbox:checked").map(function () {
            return this.value;
        }).get().join("|"));
        $("div").each(function () {
            var $this = $(this);
            $this[re.source != "" && re.test($this.attr("class")) ? "show" : "hide"]();
        });
    });


    $("#search-form").submit(function () {
        var url = "/search";
        var formdata = new FormData($(this)[0]);
        $.post({ url: url, data: formdata, contentType: false, processData: false }, function (res) {
            let lots = res["data"]
            $(".voiture").show(2)
            $(".voiture").each(function (e, datas) {
                test = false
                id = $(this).attr("id")
                for (let i of lots) {
                    if (id == i) {
                        test = true
                    }
                }
                if (!test) {
                    console.log("le id ", id)
                    $(this).hide(200)
                }
            })
        }, "json")
        return false;
    })

})