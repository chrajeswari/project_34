from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10,sal__gt=1500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='NEW YORK')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter()[:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter()[2:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Sales')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gte=1700)
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)



def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gt=2500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='king')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=1600)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='Blake')
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='Salesman')
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='Smith',sal=5000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__gt=300)
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='Manager')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lte=1600)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='Martin')
    empmgrobjects=Emp.objects.select_related('mgr').all()
    
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)



def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Accounting')|Q(ename='SCOTT'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno='30')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno='20',sal__gt=1500)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='Manager')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename='SMITH')|Q(deptno__dname='Sales'))
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno='10')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='CHICAGO')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='FORD')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal_lt=1000,comm_isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='OPERATIONS')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='salesman')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lt=1500)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='operations')|Q(ename='MARTIN'))
    emd=Emp.objects.select_related('deptno','mgr').filter(comm=500)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(comm='0')|Q(sal__gt=1000))
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='DALLAS',ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr_ename_contains='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__empno=7839)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate='2024-12-07')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr_ename_endswith='N')
    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)




def emp_salgrade(request):
   # EO=Emp.objects.all()
   # SO=SalGrade.objects.all()

   # retrieving the data of employees who belongs to  grade 4
   # SO=SalGrade.objects.filter(grade=4)

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))


    # retrieving the data of employees who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))


    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))

    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)