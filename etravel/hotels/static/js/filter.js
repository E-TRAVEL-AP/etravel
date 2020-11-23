function filter() {
    var productBox= document.getElementsByClassName('product')

    
        var fandom_filter=document.getElementById("fandom") 
        var decor_filter=document.getElementById("decor") 
        var coaster_filter=document.getElementById("coaster") 
        if(coaster_filter.dataset.status == "off"){
        for(var i = 0; i< productBox.length; i++){
           if(productBox[i].dataset.coaster == "True"){
            productBox[i].style.display=""; 
            coaster_filter.dataset.status ="on"         
           }}
        } else { 
            for(var i = 0; i< productBox.length; i++){       
           if(productBox[i].dataset.coaster == "True"){
            productBox[i].style.display="none"; 
            if(decor_filter.dataset.status == "on"){
                if(productBox[i].dataset.decor == "True"){
                    productBox[i].style.display="";
                }}
            if(fandom_filter.dataset.status == "on"){
                if(productBox[i].dataset.fandom == "True"){
                    productBox[i].style.display="";
                }}
            coaster_filter.dataset.status ="off";         
           }}
        }
    }
    function filter1() {
        var productBox= document.getElementsByClassName('product')

        
        var fandom_filter=document.getElementById("fandom") 
        var decor_filter=document.getElementById("decor") 
        var coaster_filter=document.getElementById("coaster") 
            if(decor_filter.dataset.status == "off"){
            for(var i = 0; i< productBox.length; i++){
               if(productBox[i].dataset.decor == "True"){
                productBox[i].style.display=""; 
                decor_filter.dataset.status ="on"         
               }}
            } else { 
                for(var i = 0; i< productBox.length; i++){       
               if(productBox[i].dataset.decor == "True"){
                productBox[i].style.display="none";
                if(coaster_filter.dataset.status == "on"){
                    if(productBox[i].dataset.coaster == "True"){
                        productBox[i].style.display="";
                    }}
                if(fandom_filter.dataset.status == "on"){
                    if(productBox[i].dataset.fandom == "True"){
                        productBox[i].style.display="";
                    }} 
                decor_filter.dataset.status ="off";         
               }}
            }
        }

    function filter2() {
        var productBox= document.getElementsByClassName('product')

        
            var fandom_filter=document.getElementById("fandom") 
            var decor_filter=document.getElementById("decor") 
            var coaster_filter=document.getElementById("coaster") 
            if(fandom_filter.dataset.status == "off"){
            for(var i = 0; i< productBox.length; i++){
                if(productBox[i].dataset.fandom == "True"){
                productBox[i].style.display=""; 
                fandom_filter.dataset.status ="on"         
                }}
            } else { 
                for(var i = 0; i< productBox.length; i++){       
                if(productBox[i].dataset.fandom == "True"){
                productBox[i].style.display="none";
                if(decor_filter.dataset.status == "on"){
                    if(productBox[i].dataset.decor == "True"){
                        productBox[i].style.display="";
                    }}
                if(coaster_filter.dataset.status == "on"){
                    if(productBox[i].dataset.coaster == "True"){
                        productBox[i].style.display="";
                    }}
                fandom_filter.dataset.status ="off";         
                }}
            }
        }