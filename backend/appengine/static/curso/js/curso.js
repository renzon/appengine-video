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
        },
        controller:function($scope, $http){
            $scope.salvar=function(){
                $http.post('/courses/rest/new',$scope.course).success(function(course){
                    console.log(course);
                }).error(function(erros){
                    console.log(errors);
                });
            }

        }
    };
});