import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Root } from "../Root";
import { About } from "@/pages/About";
import { EnterprisesAndIndustries } from "@/pages/EnterprisesAndIndustries";
import { SignIn } from "@/pages/auth/SignIn";
import { RestorePassword } from "@/pages/auth/RestorePassword";
import { PasswordRestoreSuccess } from "@/pages/auth/PasswordRestoreSuccess";
import { SignUp } from "@/pages/auth/SignUp";
import { ForgotPassword } from "@/pages/auth/ForgotPassword";
import { PasswordRecoveryEmailSent } from "@/pages/auth/PasswordRecoveryEmailSent";

const routes = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/enterprises-and-industries",
        element: <EnterprisesAndIndustries />,
      },
      {
        path: "/signin",
        element: <SignIn />,
      },
      {
        path: "/reset-password",
        element: <RestorePassword />,
      },
      {
        path: "/password-restore-success",
        element: <PasswordRestoreSuccess />,
      },
      {
        path: "/signup",
        element: <SignUp />,
      },
      {
        path: "/forgot-password",
        element: <ForgotPassword />,
      },
      {
        path: "/password-recovery-email-sent",
        element: <PasswordRecoveryEmailSent />,
      },
    ],
  },
]);

export function Router() {
  return <RouterProvider router={routes} />;
}
