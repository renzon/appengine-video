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
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                $http.post('/courses/rest/new',$scope.course).success(function(course){
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