import React from 'react';
import { Breadcrumb } from 'antd';
import Link from 'next/link';
const App = () => (
  <Breadcrumb
    items={[
      {
        title: <Link href=".">Home</Link>,
      },
      {
        title: <Link href="./bc">BC</Link>,
      },
      {
        title: <Link href="./ab">AB</Link>,
      },
      {
        title: <Link href="./sk">SK</Link>,
      },
      {
        title: <Link href="./mb">MB</Link>,
      },
      {
        title: <Link href="./on">ON</Link>,
      },
      {
        title: <Link href="./qc">QC</Link>,
      },
      {
        title: <Link href="./nb">NB</Link>,
      },
      {
        title: <Link href="./nl">NL</Link>,
      },
      {
        title: <Link href="./ns">NS</Link>,
      },
    ]}
  />
);
export default App;