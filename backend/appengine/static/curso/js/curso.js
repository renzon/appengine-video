var cursoModulo=angular.module('cursoModulo',['rest']);

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
        controller:function($scope, CursoApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                CursoApi.salvar($scope.course).success(function(course){
                    console.log(course);
                    $scope.course.title='';
                    $scope.course.price='';
                    $scope.salvandoFlag=false;
                }).error(function(errors){
                    $scope.errors=errors;
                    console.log(errors);
                    $scope.salvandoFlag=false;
                });


            }

        }
    };
});