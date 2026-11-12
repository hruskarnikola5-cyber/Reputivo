(function(){
'use strict';
var b=document.querySelectorAll('#showcaseChat .chat-bubble'),se=document.getElementById('showcaseStatus'),pe=document.getElementById('showcasePill'),ds=document.querySelectorAll('#demoSteps .demo-dot'),pb=document.getElementById('demoPrev'),plb=document.getElementById('demoPlay'),nb=document.getElementById('demoNext'),rb=document.getElementById('demoRestart');
if(!b.length)return;
var t=b.length,c=0,playing=false,pi;
function s(i){
  b.forEach(function(b2,i2){b2.classList.toggle('visible',i2<=i);b2.style.position=i2<=i?'relative':'absolute';});
  ds.forEach(function(d,i2){d.classList.toggle('active',i2<=i);});
  if(se)se.textContent='Schritt '+(i+1)+' von '+t;
  if(pe){pe.textContent=i>=t-1?'Veröffentlicht':'bereit';pe.className='pill '+(i>=t-1?'pill-published':'pill-default');}
  c=i;pb.disabled=i===0;if(nb)nb.disabled=i>=t-1;
}
function nx(){if(c<t-1)s(c+1);else stop();}
function pv(){if(c>0)s(c-1);}
function stop(){if(pi){clearInterval(pi);pi=null;}playing=false;if(plb)plb.textContent='▶';}
function play(){if(c>=t-1)s(0);playing=true;if(plb)plb.textContent='⏸';pi=setInterval(function(){if(c<t-1)s(c+1);else stop();},3000);}
function restart(){stop();s(0);}
if(pb)pb.addEventListener('click',function(){stop();pv();});
if(nb)nb.addEventListener('click',function(){stop();nx();});
if(plb)plb.addEventListener('click',function(){playing?stop():play();});
if(rb)rb.addEventListener('click',restart);
s(0);
})();