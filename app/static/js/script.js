// ==========================================================
// RESPONSE TYPE SWITCHING
// ==========================================================


const responseTypes = document.querySelectorAll(
    'input[name="type"]'
);


const textSection =
document.getElementById("text-section");


const pdfSection =
document.getElementById("pdf-section");


const voiceSection =
document.getElementById("voice-section");




responseTypes.forEach(type => {


    type.addEventListener(
        "change",
        function(){


            // Hide all sections

            textSection.classList.add("hidden");

            pdfSection.classList.add("hidden");

            voiceSection.classList.add("hidden");




            // Show selected section


            if(this.value === "text"){


                textSection.classList.remove("hidden");


            }



            else if(this.value === "pdf"){


                pdfSection.classList.remove("hidden");


            }



            else if(this.value === "voice"){


                voiceSection.classList.remove("hidden");


            }



        }

    );


});







// ==========================================================
// PDF FILE NAME DISPLAY
// ==========================================================


const pdfInput =
document.getElementById("pdf-file");



pdfInput.addEventListener(
"change",
function(){


    if(this.files.length > 0){


        const fileName =
        this.files[0].name;



        document.querySelector(
            ".upload-area p"
        ).innerHTML =
        fileName;



    }


});








// ==========================================================
// VOICE RECORDING
// ==========================================================



const micButton =
document.getElementById("mic-button");


const voiceStatus =
document.getElementById("voice-status");



let mediaRecorder;

let audioChunks = [];

let recording = false;


let timer;

let seconds = 0;







micButton.addEventListener(
"click",
async function(){



    if(!recording){


        startRecording();


    }

    else{


        stopRecording();


    }



});









async function startRecording(){


    try{


        const stream =
        await navigator.mediaDevices.getUserMedia(
            {
                audio:true
            }
        );



        mediaRecorder =
        new MediaRecorder(stream);



        audioChunks = [];



        mediaRecorder.start();



        recording = true;



        micButton.style.animation =
        "pulse 1s infinite";



        voiceStatus.innerHTML =
        "🔴 Recording started...";



        startTimer();




        mediaRecorder.ondataavailable =
        event =>{


            audioChunks.push(
                event.data
            );


        };




        mediaRecorder.onstop =
        ()=>{


            const audioBlob =
            new Blob(
                audioChunks,
                {
                    type:"audio/webm"
                }
            );



            console.log(
                "Recorded Audio:",
                audioBlob
            );



            voiceStatus.innerHTML =
            "✅ Voice recorded successfully";



        };




    }


    catch(error){


        alert(
            "Microphone permission denied"
        );


        console.log(error);


    }


}









function stopRecording(){


    mediaRecorder.stop();



    mediaRecorder.stream
    .getTracks()
    .forEach(
        track=>track.stop()
    );



    recording=false;



    micButton.style.animation =
    "none";



    stopTimer();



}









// ==========================================================
// RECORDING TIMER
// ==========================================================



function startTimer(){


    seconds=0;


    timer=setInterval(
        ()=>{


            seconds++;


            let min =
            Math.floor(seconds/60);



            let sec =
            seconds%60;



            voiceStatus.innerHTML =

            `🔴 Recording ${min}:${sec < 10 ? 
            "0"+sec : sec}`;



        },
        1000
    );

}




function stopTimer(){


    clearInterval(timer);


}









// ==========================================================
// EVALUATE BUTTON
// REDIRECT TO RESULTS PAGE
// ==========================================================



const evaluateButton =
document.getElementById(
    "evaluate-button"
);





evaluateButton.addEventListener(
"click",
function(){



    const question =
    document.getElementById(
        "question"
    ).value;



    if(question.trim()===""){


        alert(
            "Please enter your question"
        );


        return;


    }




    // Later we send data to FastAPI API

    // For Milestone 1 only redirect


    window.location.href =
    "/results";



});
