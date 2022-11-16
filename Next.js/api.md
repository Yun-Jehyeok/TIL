# API folder in NextJS

NextJS는 React의 Framework 로 나왔지만 Client만 지원하는 것은 아니다.

pages/api 폴더를 만들어 여기서 Server API를 생성할 수도 있다.

next 자체에서 NextApiRequest와 NextApiResponse 타입을 지원하기 때문에 이를 사용하면 되며

예를 들어 pages/api/test.tsx 라는 파일을 만들고 작업을 했다면 http://localhost:port/api/test 에 접속하는 것으로 확인이 가능하다.

코드는 아래와 같이 짤 수 있다.

```
import { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  await 함수함수();

  res.json({
    ok: true,
  });
}
```
