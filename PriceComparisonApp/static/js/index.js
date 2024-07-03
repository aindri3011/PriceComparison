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


   $(document).on("click",".search_btn",function () {

              let search_bar = document.getElementById("search_bar").value

     mydata = {
         "search_bar":search_bar,

     }


    $.ajax({
        url: `search-product`,
        method: "POST",
        headers: {'X-CSRFToken': document.getElementById('csrf').querySelector('input').value},
        data : mydata,
        success: (res)=>{

           // console.log(res)
            if(res.status == 1) {
                $("#product_row").empty();
                const productRow = document.getElementById('product_row');


                Object.entries(res.return_data).forEach(([storeName, items]) => {
        const storeHtml = `
            <div class="card" style="width: 18rem; background: #fdadf0;">
                <div class="card-body">
                    <h5 class="card-title" style="color: #b00a95;">${storeName}</h5>
                    <hr>
                    <ul>
                        ${items.map(item => `
                            <li>
                            <button type="button" onclick="location.href='/product_details/?product_id=${item.product_id}'"
                                   class="btn btn-default" style="color: white; background: #86008b; margin: 2px;">${item.product} - Rs. ${item.price}</button>
                                
                            </li>
                        `).join('')}
                    </ul>
                </div>
            </div>
        `;

        productRow.insertAdjacentHTML('beforeend', storeHtml);
    });
}




            else{
                alert("Something Went Wrong...")
            }
        },
        error: (error)=>{
            console.log(error)
            alert("Something went wrong...")
        }
    })

    });

