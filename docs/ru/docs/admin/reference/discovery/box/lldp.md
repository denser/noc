# LLDP

`Low Level Discovery Protocol`. Топологический протокол стандарта `IEEE 802.1AB-2009`. 
Благодаря своей независимости позволяет строить связи между оборудованием разных производителей. 
Взамен получаем сложность и головоломность работы. В частности есть 7 форматов передачи `Chassis ID` и 7 форматов передачи интерфейса соседа.

Основная сложность в работе с LLDP - различные форматы представления ID порта. Например:

1) Имя. Имя отображаемое по LLDP может отличаться от имени, используемого на оборудовании.
2) MAC адрес. Часто можно встретить ситуацию, когда интерфейсам устройства присвоен одинаковый MAC адрес (см. `DLink`), 
что делает невозможным определение порта подключения. 
В таких случаях система может попытаться соориентироваться по описанию (`description`) порта, но для этого он должен отличаться от остальных.
3) Локальный ID. Обычно, в этим случаях передаётся `snmp_index`. Поэтому в системе он должен быть заполнен для интерфейсов устройства

## Требования

* Скрипт [get_lldp_neighbors](../../../../dev/sa/scripts/get_lldp_neighbors.md)
* Возможность [Network LLDP caps](../../../../user/reference/caps/network/lldp.md)
* Опрос LLDP включён в профиле объектов [Managed Object Profile](../../../../user/reference/concepts/managed-object-profile/index.md#Box(Полный_опрос))
* Метод LLDP в *Методах построения топологии* [Segment Profile](../../../../user/reference/concepts/network-segment-profile/index.md)
