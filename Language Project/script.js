// script.js

// Wait for the HTML document to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get all the navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
  
    // Attach click event listeners to each navigation link
    navLinks.forEach(function(link) {
      link.addEventListener('click', function(event) {
        // Prevent the default link behavior
        event.preventDefault();
  
        // Get the target URL from the clicked link's href attribute
        const targetUrl = this.getAttribute('href');
  
        // Redirect to the target URL
        window.location.href = targetUrl;
      });
    });

 

  });

//   Below is a test function that adds two numbers. we can ignore it
  function addNumbers() {
    // Get the values from the input fields
    var num1 = parseInt(document.getElementById('num1').value);
    var num2 = parseInt(document.getElementById('num2').value);
  
    // Add the numbers together
    var sum = num1 + num2;
  
    // Display the result
    document.getElementById('result').textContent = 'Result: ' + sum;
  }

  //Array of images
  
  //Change image func below
  function changeImage(imageSource) {
    var img = document.getElementById('image');
    img.src = imageSource;
  }
  function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  function randomFunc() {
    var stringsArray = ["barca.jpeg", "String 2", "String 3"];
    var x = getRandomNumber(0, stringsArray.length)
    
    var img = document.getElementById('image')
    img.src = stringsArray[x];
  }


  //Below is code for fetching from python. 
  fetch('/get_response')
  .then(response => response.json())
  .then(data => {
    // Process the response data
    console.log(data);
    // Update the UI with the received response
    document.getElementById('response-container').innerHTML = data.response;
  })
  .catch(error => {
    // Handle any errors that occurred during the API call
    console.error('Error:', error);
  });

  //Below is code for the popup
  function showOverlay() {
    document.getElementById("overlay").style.display = "block";
  }
  
  function hideOverlay() {
    document.getElementById("overlay").style.display = "none";
  }

  function processInput() {
    var img = document.getElementById('image');
    img.src = "textInput";
  }



  //BELOW IS ALL GPT RELATED BUSINESS
  const apiKey = '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'; // Replace with your actual API key
  const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions';
  const resultElement = document.getElementById('result');
  
  async function generateGPTQuery(prompt) {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        prompt: prompt,
        max_tokens: 50, // Adjust the desired number of tokens in the response
      }),
    });
  
    const data = await response.json();
    const generatedQuery = data.choices[0].text.trim();
  
    resultElement.textContent = generatedQuery; // Update the HTML content
  }
  
  const prompt = 'Once upon a time'; // Replace with your desired prompt
  
  generateGPTQuery(prompt)
    .catch((error) => {
      console.error('Error:', error);
    });