var updateBtns= document.getElementsByClassName('update-wishlist')

for(var i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId =  this.dataset.product
        var action = this.dataset.waction
        console.log('productId:', productId, 'action:', 'action')

        console.log('USER:', user)

        if(user ==='AnonymousUser'){
            console.log('User is not authenticatedn')
        }
        else{
            updateUserWishlistOrder(productId, action)
        }
        
    })


}

function updateUserWishlistOrder(productId, action){
    console.log('User is Authenticated, sneding data to wishlist')

    var url = '/update_wishlist_item/'

    // var url = window.location.hostname + 'update_item/'
    // console.log(window.location.hostname + 'update_item/')
    // console.log(JSON.stringify({'productId':productId, 'action':action}))
    // console.log('helloo1')
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}
