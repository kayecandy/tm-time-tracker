



class CndceLoader{
    $cndceLoader;
    $cndceTypewriter;
    loadQueue = [];
    iLoadQueue = 0;

    constructor(){
        
    }

    __initDom(){
        this.$cndceLoader = $('.cndce-loader');
        this.$cndceTypewriter = $('.cndce-typewriter');
    }

    addLoadQueue(promise){
        this.loadQueue.push(promise);

        promise.then(()=>{
            this.iLoadQueue++;

            if(this.loadQueue.length == this.iLoadQueue){
                this.finishLoading();
            }
        })
    }

    finishLoading(){
        this.$cndceTypewriter.html('LOADED');

        this.$cndceTypewriter.css({
            'animation': 'unset'
        })
        
    
        this.$cndceTypewriter.animate({
            width: '26rem'
        }, {
            duration: 200,
            complete: ()=>{
                setTimeout(()=>{
                    this.$cndceLoader.fadeOut(150, function (e){
                        console.log("loaded");
                    })
                }, 300)
            }
        })
            // $('.cndce-loader').remove()
    }
}

window.CNDCE = {
    loader: new CndceLoader()
}

CNDCE.loader.addLoadQueue(new Promise((resolve, rej)=>{
    $(window).on('load', function(){

        CNDCE.loader.__initDom()
        resolve()
     
        
    })  
}))

