(function(){
'use strict';
document.querySelectorAll('.faq-question').forEach(function(b){
  b.addEventListener('click',function(){
    var i=b.parentElement,o=i.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function(oi){
      if(oi!==i){oi.classList.remove('open');oi.querySelector('.faq-question').setAttribute('aria-expanded','false');}
    });
    i.classList.toggle('open',!o);b.setAttribute('aria-expanded',!o);
  });
  b.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();b.click();}});
});
})();