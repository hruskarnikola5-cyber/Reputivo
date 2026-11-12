(function(){
'use strict';
var hb=document.getElementById('hamburger'),nl=document.getElementById('navLinks');
if(hb&&nl){hb.addEventListener('click',function(){var o=nl.classList.toggle('open');hb.classList.toggle('active');hb.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':'';});nl.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nl.classList.remove('open');hb.classList.remove('active');hb.setAttribute('aria-expanded','false');document.body.style.overflow='';});});}
var tb=document.getElementById('topbar'),st=false;window.addEventListener('scroll',function(){if(!st){requestAnimationFrame(function(){tb.classList.toggle('scrolled',window.scrollY>20);st=false;});st=true;}},{passive:true});
if(!window.matchMedia('(prefers-reduced-motion:reduce)').matches){var rvs=document.querySelectorAll('.reveal'),ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');ro.unobserve(e.target);}});},{threshold:0.12,rootMargin:'0px 0px -40px 0px'});rvs.forEach(function(el){ro.observe(el);});}
})();
