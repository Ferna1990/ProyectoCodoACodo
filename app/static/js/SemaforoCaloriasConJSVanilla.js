
let datatable;
let datatableisinit= false;


const datatableoptions ={
    columnDefs:[
        {className:'centered', targets:[0,1,2,3,4]},
        {orderable: false, targets:[4]},
        {searchable: false, targets:[1,2,3,4]},

    ]
};


const initdatatable = async()=>{
if(datatableisinit){
    datatable.destroy();
}
await listproducto();

datatable = $('#datatable-productos').Datatable(datatableoptions);

datatableisinit=true;
}


const listproducto=async()=>{
    try{
        const response=await fetch ('http://127.0.0.1:8000/app/list_productos/');
        const data=await response.json();
        let content=``;
        data.producto.forEach((producto,index)=>{            
            content+=`
                <tr>
                    <td>${index+1}</td>
                    <td>${producto.nombre}</td>
                    <td>${producto.calorias}</td>
                    <td>${producto.color}</td>
                </tr>
            `;
        });
        tablebody_producto.innerHTML = content;

    }catch(ex){
        alert(ex);
    }
};
window.addEventListener('load',async()=>{
await initdatatable();
});

