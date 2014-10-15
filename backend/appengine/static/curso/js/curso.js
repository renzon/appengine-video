var cursoModulo=angular.module('cursoModulo',[]);

cursoModulo.directive('cursoform',function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl:'/static/curso/html/curso_form.html',
        scope:{
            course: '=',
            priceLabel: '@',
            titleLabel: '@'
        }
    };
});