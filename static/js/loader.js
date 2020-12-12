$(window).on('load', function(){


    $('.cndce-typewriter').css({
        'animation': 'unset'
    })

    $('.cndce-typewriter').animate({
        width: '26rem'
    }, {
        duration: 200,
        complete: function(){
            setTimeout(function(){
                $('.cndce-loader').fadeOut(150, function (e){
                    console.log("loaded");
                })
            }, 300)
        }
    })
        // $('.cndce-loader').remove()
        
    
})