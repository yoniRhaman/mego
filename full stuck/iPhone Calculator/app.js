// DOM Elements
const hourEl = document.querySelector('.hour');
const minuteEl = document.querySelector('.minute');

// Function to update the time
const updateTime = () => {
    // Get the current time
    const currentTime = new Date();

    // Extract hours and minutes
    const currentHour = currentTime.getHours();
    const currentMinute = currentTime.getMinutes();

    // Update the content of HTML elements
    hourEl.textContent = currentHour.toString();
    minuteEl.textContent = currentMinute.toString();
}

// Update the time every second
setInterval(updateTime, 1000);

// Initial call to set the time immediately
updateTime();

