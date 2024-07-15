$(document).ready(function(){
    $('#add-cart').click(function(event){
        event.preventDefault();
        console.log("Button Clicked");

        var product_id = $('#add-cart').val();
        console.log(product_id)

        var product_qty = $('#product-qty').val();
        console.log(product_qty)

        var url = $('#add-cart').data('url');

        var csrf = '{{ csrf_token }}';

        $.ajax({
            type : 'POST',
            url : url,
            headers : {
                'X-CSRFToken': csrf,
            },
            data : {
                product_id : product_id,
                product_qty : product_qty,
                action : 'post'
            },
            success : function(json){
             console.log(json)
             $('#cart-quantity').text(json.quantity);
            },
            error : function(error , errmsg){
                console.log("Error ocurred :" , errmsg , err)

            }

        })

    })
});
