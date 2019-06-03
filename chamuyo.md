#Patron Master-Slave

La replicación master slave nos permite tener varias copias sincronicas de nuestra base de datos principal,
cualquier cambio en el Master se replicará en los slaves, esta configuración nos proporciona escalabilidad y backup, entre otras cosas, como por ejemplo hacer consultas sobre la réplica sin afectar a la base de datos principal.
Su objetivo es utilizar un servidor principal (master) para la escritura y otro o varios (slaves) para la lectura,
esto nos da un mejor rendimiento y mayor fluidez al momento de esperar una respuesta de este. 
#aca el porque es para esta app

                                               
                Arquitectura Master-slave
                                                               
                                        |||||||             |||||||                      
                          |-----------> |slave|-----------> |slave|                
    ||||||||||||          |             |||||||             |||||||                      
    ||||||||||||          |                                                                                         
    ||||||||||||          |                                                                                            
    ||||||||||||          |             |||||||                                                                       
    |||master|||----------|-----------> |slave|                                                                       
    ||||||||||||          |             |||||||                                                                        
    ||||||||||||          |                                                                 
    ||||||||||||          |                                                                 
    ||||||||||||          |             |||||||                                                       
                          |-----------> |slave| 
                                        |||||||    




#Patron Multi-Master

A diferencia del patron Master-slave en este caso todos los servidores trabajan como maestros y esclavos,
siendo que la misma base de datos sirve para lectura y escritura.
La replicación de múltiples Master es un método que permite que los datos sean almacenados por un grupo de servidores, y actualizados por cualquier miembro del grupo. Todos los miembros responden a las consultas. El sistema de replicación con múltiples maestros es responsable de enviar las modificaciones de datos realizadas por cada miembro al resto del grupo.
#aca el porque es para esta app



                     Arquitectura MultiMaster

          |---------------------|---------------------|                              
          |                     |                     |                                                              
    ||||||||||||          ||||||||||||          ||||||||||||                                                       
    ||||||||||||          ||||||||||||          ||||||||||||                                      
    ||||||||||||          ||||||||||||          ||||||||||||                                    
    ||||||||||||          ||||||||||||          ||||||||||||                                             
    |||master|||<-------->|||master|||<-------->|||master|||                                                       
    ||||||||||||          ||||||||||||          ||||||||||||                                                
    |||slave||||          |||slave||||          |||slave||||                                             
    ||||||||||||          ||||||||||||          ||||||||||||                                             
    ||||||||||||          ||||||||||||          ||||||||||||                                                   
          ^                     ^                     ^
          |                     |                     |
          |---------------------|---------------------|
