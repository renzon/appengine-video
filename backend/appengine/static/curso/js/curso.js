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
                var promessa = CursoApi.salvar($scope.course);
                promessa.success(function(course){
                    console.log(course);
                    $scope.course.title='';
                    $scope.course.price='';
                    $scope.salvandoFlag=false;
                })
                promessa.error(function(errors){
                    $scope.errors=errors;
                    console.log(errors);
                    $scope.salvandoFlag=false;
                });


            }

        }
    };
});

cursoModulo.directive('cursolinha',function(){
    return{
        replace:true,
        templateUrl:'/static/curso/html/curso_linha_tabela.html',
        scope:{
            course: '='
        },
        controller:function($scope, CursoApi){


        }
    };
});