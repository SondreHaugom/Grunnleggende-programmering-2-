from pytest import mark
from verktoy import finn_minste_storste


@mark.parametrize(
    "tall, forventet_minste, forventet_storste",
    [
        ([3, 1, 4, 1, 5, 9, 2], (1, 9)),      
        ([-5, -1, -10, -2], (-10, -1)),       
        ([0, 0, 0, 0], (0, 0)),              
        ([42], (42, 42)),                    
        ([1.5, 2.7, -0.5, 4.2], (-0.5, 4.2)), 

    ]
)