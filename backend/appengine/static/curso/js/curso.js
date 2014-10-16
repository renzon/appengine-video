var cursoModulo = angular.module('cursoModulo', ['rest']);

cursoModulo.directive('cursoform', function () {
    return{
        restrict: 'E',
        replace: true,
        templateUrl: '/static/curso/html/curso_form.html',
        scope: {
            course: '=',
            priceLabel: '@',
            titleLabel: '@',
            saveComplete: '&'
        },
        controller: function ($scope, CursoApi) {
            $scope.salvandoFlag = false;
            $scope.salvar = function () {
                $scope.salvandoFlag = true;
                $scope.errors = {};
                var promessa = CursoApi.salvar($scope.course);
                promessa.success(function (course) {
                    $scope.course.title = '';
                    $scope.course.price = '';
                    $scope.salvandoFlag = false;
                    if ($scope.saveComplete != undefined) {
                        $scope.saveComplete({'curso': course});
                    }
                })
                promessa.error(function (errors) {
                    $scope.errors = errors;
                    $scope.salvandoFlag = false;
                });


            }

        }
    };
});

cursoModulo.directive('cursolinha', function () {
    return{
        replace: true,
        templateUrl: '/static/curso/html/curso_linha_tabela.html',
        scope: {
            course: '=',
            deleteComplete: '&'
        },
        controller: function ($scope, CursoApi) {
            $scope.ajaxFlag = false;
            $scope.editingFlag = false;
            $scope.cursoEdicao = {}
            $scope.deletar = function () {
                $scope.ajaxFlag = true;
                CursoApi.deletar($scope.course.id).success(function () {
                    $scope.deleteComplete({'curso': $scope.course});
                }).error(function () {
                    console.log('erro');
                });
            }

            $scope.editar = function () {
                $scope.editingFlag = true;
                $scope.cursoEdicao.id = $scope.course.id
                $scope.cursoEdicao.title = $scope.course.title
                $scope.cursoEdicao.price = $scope.course.price
            }

            $scope.cancelar = function () {
                $scope.editingFlag = false;
            }

            $scope.completarEdicao = function () {
                CursoApi.editar($scope.cursoEdicao).success(function (course) {
                    $scope.course = course;
                    $scope.editingFlag = false;
                });
            }

        }
    };
});