



// JavaScript to control popup visibility
 document.addEventListener('DOMContentLoaded', ()=>{
    const openModel = document.getElementById('modelOpen');
    const model = document.getElementById('model');
    const closeModel = document.getElementById('closeModel');


    openModel.addEventListener('click', ()=>{
        model.classList.remove('hidden')
        // model.classList.add('transition 300ms')
    })

    closeModel.addEventListener('click', ()=>{
        model.classList.add('hidden')
    })

 })


// sidebar toggle function 
function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("hidden");
}

// JavaScript to handle dropdown toggle
   function toggleDropdown() {
    var dropdownMenu = document.getElementById("dropdown-menu");
    dropdownMenu.classList.toggle("hidden");
   }
    
    
// Function to update the clock
// Function to update the clock
function updateClock() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    // Format time with leading zeros if necessary
    const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

    // Format date
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

    // Display the formatted time and date
    document.getElementById('clock').innerText = formattedTime;
    document.getElementById('date').innerText = formattedDate;
}

// Call updateClock function every second
setInterval(updateClock, 1000);

// Initial call to display the time immediately
updateClock();