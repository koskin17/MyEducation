import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/libs/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 hover:cursor-pointer font-semibold whitespace-nowrap rounded-sm transition-all disabled:cursor-not-allowed disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        primary:
          "px-4 py-2.5 text-main-white bg-main-gray-100 hover:bg-primary-hover disabled:bg-inactive-80 disabled:text-inactive-100 text-sm md:text-[16px]",
        destructive:
          "px-4 py-2.5 text-main-white bg-primary-red hover:bg-primary-red-hover disabled:bg-inactive-80 disabled:text-inactive-100",
        secondary:
          "px-4 py-2.5 text-secondary-black hover:bg-secondary-beige outline-1 outline-secondary-black disabled:bg-inactive-80 disabled:text-inactive-100 disabled:outline-inactive-100",
        tertiary:
          "text-main-black hover:underline hover:underline-offset-4 disabled:no-underline",
      },
    },
    defaultVariants: {
      variant: "primary",
    },
  }
);

function Button({
  className,
  variant,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean;
  }) {
  const Comp = asChild ? Slot : "button";

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, className }))}
      {...props}
    />
  );
}

export { Button, buttonVariants };
