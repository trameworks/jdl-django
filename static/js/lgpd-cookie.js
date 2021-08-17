var options = {
    title: 'Política de privacidade',
    message: 'Olá, utilizamos cookies para registrar os acessos ao nosso site de acordo com a Lei Geral de Proteção de Dados Pessoais (LGPD). Guardamos as informações de navegação apenas para registro histórico das edições do festival.',
    delay: 600,
    expires: 30,
    link: '/',
    onAccept: function(){
        var myPreferences = $.fn.ihavecookies.cookie();
        console.log('Yay! The following preferences were saved...');
        console.log(myPreferences);
    },
    uncheckBoxes: true,
    acceptBtnLabel: 'Aceitar Cookies',
    moreInfoLabel: 'Mais informações',
    cookieTypesTitle: 'Escolha os cookies que você desejar',
    fixedCookieTypeLabel: 'Essencial',
    fixedCookieTypeDesc: 'Essencial para o funcionamento do site.',
    advancedBtnLabel: 'Avançado',
    cookieTypes: [
        {
            type: 'Analytics',
            value: 'analytics',
            description: 'Relacionados as suas visitas, tipo de navegador e informações coletadas pelo Google.'
        }
    ]
}

$(document).ready(function() {
    $('body').ihavecookies(options);

});
