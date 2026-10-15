/* Google Analytics 4, loaded only after the visitor accepts. The measurement ID comes from data-ga on this script tag. */
(function(){
  var s=document.currentScript, id=s&&s.getAttribute('data-ga');
  if(!id)return;
  var KEY='sn-consent', loaded=false, bar=null;
  function get(){try{return localStorage.getItem(KEY);}catch(e){return null;}}
  function set(v){try{localStorage.setItem(KEY,v);}catch(e){}}
  function load(){
    if(loaded)return; loaded=true;
    window.dataLayer=window.dataLayer||[];
    window.gtag=function(){window.dataLayer.push(arguments);};
    window.gtag('js',new Date());
    window.gtag('config',id);
    var g=document.createElement('script');
    g.async=true; g.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(id);
    document.head.appendChild(g);
  }
  function clearCookies(){
    var host=location.hostname, root=host.split('.').slice(-3).join('.');
    document.cookie.split(';').forEach(function(c){
      var n=c.split('=')[0].trim();
      if(n.indexOf('_ga')===0||n.indexOf('_gid')===0){
        ['', ';domain='+host, ';domain=.'+host, ';domain=.'+root].forEach(function(d){
          document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/'+d;
        });
      }
    });
  }
  function hide(){if(bar){bar.parentNode.removeChild(bar);bar=null;}}
  function show(){
    if(bar)return;
    bar=document.createElement('div');
    bar.className='consent'; bar.setAttribute('role','region'); bar.setAttribute('aria-label','Cookie choice');
    bar.innerHTML='<p>Can we use Google Analytics cookies to see which pages help visitors? Nothing loads unless you accept. <a href="/privacy/">Privacy policy</a></p>'+
      '<div class="consent-btns"><button type="button" class="btn ghost" data-c="no">Decline</button><button type="button" class="btn" data-c="yes">Accept</button></div>';
    bar.addEventListener('click',function(e){
      var c=e.target&&e.target.getAttribute&&e.target.getAttribute('data-c');
      if(!c)return;
      if(c==='yes'){set('granted');load();hide();}
      else{set('denied');clearCookies();hide();if(loaded)location.reload();}
    });
    document.body.appendChild(bar);
  }
  var v=get();
  if(v==='granted')load();
  else if(v!=='denied'){
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',show);else show();
  }
  document.addEventListener('click',function(e){
    var t=e.target&&e.target.closest&&e.target.closest('[data-cookie-settings]');
    if(t){e.preventDefault();show();}
  });
})();
