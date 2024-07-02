 $(document).ready(function () {
          $('.loader1').hide();
 $(document).ajaxStart(function () {
        $('.loader1').show();
    });
    $(document).ajaxStop(function () {
        $('.loader1').hide();
    });
    $(document).ajaxError(function () {
        $('.loader1').hide();
    });
});

 $(document).on("click",".store_btn",function () {

              let store_name = document.getElementById("add_store").value

     mydata = {
         "store_name":store_name,

     }
     console.log(mydata)
    $.ajax({
        url: `add-shop`,
        method: "POST",
        headers: {'X-CSRFToken': document.getElementById('csrf').querySelector('input').value},
        data : mydata,
        success: (res)=>{
            console.log(res)
            if(res.status == 1){
                location.reload();
                alert("Store Created")
            }else{
                alert("Something Went Wrong...")
            }
        },
        error: (error)=>{
            console.log(error)
            alert("Something went wrong...")
        }
    })

    });

  $(document).on("click",".product_btn",function () {

              let store_name = document.getElementById("store").value
              let item = document.getElementById("item").value
             let price = document.getElementById("price").value
     mydata = {
         "store_name":store_name,
         "item": item,
         "price": price
     }

    $.ajax({
        url: `add-product`,
        method: "POST",
        headers: {'X-CSRFToken': document.getElementById('csrf').querySelector('input').value},
        data : mydata,
        success: (res)=>{
            console.log(res)
            if(res.status == 1){
                location.reload();
                alert("Product Created")
            }else{
                alert("Something Went Wrong...")
            }
        },
        error: (error)=>{
            console.log(error)
            alert("Something went wrong...")
        }
    })

    });