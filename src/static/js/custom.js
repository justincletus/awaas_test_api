 $(document).ready(function(){
    //  alert('I am customjs');   

    var myData = [];


    // {% for item in object_list %}
    //         myData.push([
    //             '{{ item.date|date:"Y-m-d H:m" }}',
    //             '{{ item.value }}'
    //         ]);
    // {% endfor %}

    // var myTable = $('#book-lists').DataTable({
    // order: [[0, "asc"]],
    // pageLength: 25,
    // responsive: true,
    // data: myData
    // });

    $('#book-lists').DataTable({
        order: ["asc"],
        pageLength: 10,
        responsive: true,
    });
    
 });

