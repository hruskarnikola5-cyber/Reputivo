(function(){
'use strict';
var fm=document.getElementById('contactForm'),fmg=document.getElementById('formMessage');
if(!fm)return;
fm.addEventListener('submit',function(e){
  e.preventDefault();fmg.className='form-message';fmg.textContent='';
  var n=document.getElementById('name').value.trim(),bn=document.getElementById('business').value.trim(),em=document.getElementById('email').value.trim();
  if(!n||!bn||!em){fmg.className='form-message error';fmg.textContent='Bitte füllen Sie alle Pflichtfelder aus.';return;}
  if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)){fmg.className='form-message error';fmg.textContent='Bitte geben Sie eine gültige E-Mail-Adresse ein.';return;}
  var sb=fm.querySelector('.form-submit');sb.disabled=true;sb.textContent='Wird gesendet…';
  setTimeout(function(){fmg.className='form-message success';fmg.textContent='Vielen Dank! Wir melden uns innerhalb eines Werktages.';sb.disabled=false;sb.textContent='Demo anfragen';fm.reset();},1000);
});
})();