(function(){
  // Mobile menu
  var btn=document.querySelector('.menu-btn'), nav=document.getElementById('nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.focus();}});}

  // Time-zone strip
  var cells=document.querySelectorAll('[data-tz]');
  function tick(){
    cells.forEach(function(c){
      try{c.textContent=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',hour12:false,timeZone:c.getAttribute('data-tz')}).format(new Date());}catch(e){}
    });
  }
  if(cells.length){tick();setInterval(tick,30000);}

  // Contact form (Netlify Forms, AJAX)
  var form=document.querySelector('form.contact');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var msg=form.querySelector('.form-msg');
      var data=new URLSearchParams(new FormData(form)).toString();
      msg.className='form-msg';msg.textContent='Sending…';
      fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:data})
        .then(function(r){if(!r.ok)throw new Error(r.status);
          form.reset();msg.className='form-msg ok';
          if(location.hostname.indexOf('claude')<0){location.href=form.getAttribute('action')||'/thanks/';return;}
          msg.textContent='Thanks, your brief is in. We reply within one working day.';})
        .catch(function(){msg.className='form-msg';
          msg.textContent='The form could not send from here. Please email '+form.getAttribute('data-email')+' instead.';});
    });
  }
})();
