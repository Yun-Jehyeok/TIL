// Example
interface PeopleInterface {
    name: string;
    age: number;
}
const member1: PeopleInterface = {
    name: 'yc',
    age: 34
}

type PeopleType = {
    name: string;
    age: number;
}
const member2: PeopleType = {
    name: 'yjh',
    age: 31
}

// 여기까지만 보면 딱히 차이점이 없다

///////////////////////////////////
// 차이점 1 : 확장성
// Interface 확장
interface PeopleInterface {
    name: string;
    age: number;
}
interface StudentInterface extends PeopleInterface {
    school: string;
}

// type 확장
type PeopleType2 = {
    name: string;
    age: number;
}
type StudentType = PeopleType2 & {
    school: string;
}

// 뭐.. 확장하는 방법도 차이가 있지만
// type에서는 위에서 할당한 PeopleType과 이름을 다르게 한 것처럼
// type은 같은 이름으로의 선언이 되지 않는다.
// 반면 interface는 같은 이름으로도 선언이 가능하며 항상 선언적 확장이 가능

///////////////////////////////////
// 차이점 2 : interface 는 객체에만 사용이 가능하다
// interface IFoo = string; (X)
interface IFoo {
    value: string;
}

type TFoo = string; // (O)

///////////////////////////////////
// 차이점 3 : Computed Value 사용 Type(O), Interface(X)
type names = 'firstName' | 'lastName';
type TNames = {
    [key in names]: string;
}

const yc: TNames = { firstName: 'hi', lastName: 'yc' }

// (X)
// interface IName {
//     [key in names]: string
// }

///////////////////////////////////
// 차이점 4 : 성능면에서 interface가 좋다.... 는 좀 더 찾아봐야겠다
// 이전까진 type에서 어디에 에러가 났는지 확인이 안됐지만 이제는 된다.

// 결국 결론은 type, interface 중 하나로 통일을 하라...
