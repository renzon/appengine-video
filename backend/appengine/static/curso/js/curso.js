var cursoModulo=angular.module('cursoModulo',[]);

cursoModulo.directive('cursoform',function(){
    return{
        restrict: 'E',
        replace:true,
        template:'<input type="text" />'

    };
});